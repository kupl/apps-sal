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
        
        group = n
        p, rank = list(range(n)), [0] * n
        for i in range(n):
            for j in [leftChild[i], rightChild[i]]:
                if j > -1:
                    if not union(i, j): return False
                    group -= 1
        return group == 1
