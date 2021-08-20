class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        g = defaultdict(list)
        root = set(range(n))
        for (i, (l, r)) in enumerate(zip(leftChild, rightChild)):
            g[i] += [l, r]
            root.discard(l)
            root.discard(r)
        if len(root) != 1:
            return False
        seen = set()

        def trav(cur):
            if cur in seen:
                return False
            if not g[cur]:
                return True
            seen.add(cur)
            if len(g[cur]) > 2:
                return False
            return all((trav(nxt) for nxt in g[cur]))
        if not trav(root.pop()):
            return False
        return len(seen) == n
