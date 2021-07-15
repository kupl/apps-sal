class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        def union(u, v):
            pU, pV = find(u), find(v)
            if pU == pV: return False
            rmin, rmax = (pU, pV) if rank[pU] < rank[pV] else (pV, pU)
            p[rmin] = rmax
            rank[rmax] += rank[rmin] == rank[rmax]
            return True
        
        incoming, outgoing = list(range(n)), defaultdict(list)
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            # No cycle allowed
            if l == i or r == i: return False
            if l > -1:
                # Every pair of nodes has only one edge: one-way not two-way edge
                if i in outgoing[l]: return False
                outgoing[i].append(l)
                if incoming[l] != l: return False
                incoming[l] = i
            if r > -1:
                if i in outgoing[r]: return False
                outgoing[i].append(r)
                if incoming[r] != r: return False
                incoming[r] = i
        # Only one node has no incoming edge, others have only one incoming node
        # if sum([1 for i in range(n) if incoming[i] == i]) > 1: return False
        group = n
        p, rank = list(range(n)), [0] * n
        for i in range(n):
            for j in outgoing[i]:
                if not union(i, j): return False
                group -= 1
        return group == 1
