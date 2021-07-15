class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.ranks[pv] += 1
        return True
    
    
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        uf = UnionFindSet(m*n)
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i][j] == grid[i-1][j] and not uf.union(i*n+j, (i-1)*n+j):
                    return True
                if j > 0 and grid[i][j] == grid[i][j-1] and not uf.union(i*n+j, i*n+j-1):
                    return True
        return False
