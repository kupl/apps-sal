class Solution:
    def validateBinaryTreeNodes(self, N: int, leftChild: List[int], rightChild: List[int]) -> bool:
        inNodes, outNodes = collections.defaultdict(set), collections.defaultdict(set)

        for n, c in enumerate(leftChild):
            if c != -1:
                outNodes[n].add(c)
                inNodes[c].add(n)

        for n, c in enumerate(rightChild):
            if c != -1:
                outNodes[n].add(c)
                inNodes[c].add(n)

        zeroInDegree = 0
        root = None
        for i in range(N):
            if len(inNodes[i]) > 1:
                return False
            if not inNodes[i]:
                root = i
                zeroInDegree += 1

        if zeroInDegree != 1:
            return False

        def hasCycle(n, visited):
            visited.add(n)
            for nb in outNodes[n]:
                if nb in visited:
                    return True
                if hasCycle(nb, visited):
                    return True
            return False

        visited = set()
        if hasCycle(root, visited):
            return False
        if len(visited) != N:
            return False

        return True
