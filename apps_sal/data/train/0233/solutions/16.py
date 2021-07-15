class UnionFind:
    def __init__(self, N):
        self.par = list(range(N))
        self.rank = [0]*N
        
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px==py: return
        
        if self.rank[px]<self.rank[py]:
            self.par[px] = py
        elif self.rank[px]>self.rank[py]:
            self.par[py] = px
        else:
            self.par[py] = px
            self.rank[px] += 1
        
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        uf = UnionFind(4*N*N)
        
        for i in range(N):
            for j in range(N):
                idx = 4*(i*N+j)
                if grid[i][j]!='/':
                    uf.union(idx, idx+1)
                    uf.union(idx+2, idx+3)
                if grid[i][j]!='\\\\':
                    uf.union(idx, idx+3)
                    uf.union(idx+1, idx+2)

                if i:
                    uf.union(idx, idx-4*N+2)
                if j:
                    uf.union(idx+3, idx-4+1)
        # print(uf.par)
        return sum(uf.find(x)==x for x in range(4*N*N))
