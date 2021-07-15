class DSU:
    def __init__(self,m,n):
        self.par = {(i,j):(i,j) for i in range(m) for j in range(n)}
    
    def find(self,x):
        if self.par[x]!=x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        if xp == yp:
            return False
        self.par[xp] = yp
        return True

dirs = [(0,1),(1,0)]
class Solution:
    def containsCycle(self, grid):
        R,C = len(grid),len(grid[0])
        dsu = DSU(R,C)        
        for r in range(R):
            for c in range(C):
                for x,y in dirs:
                    nr,nc = r+x,c+y
                    if 0<=nr<R and 0<=nc<C and grid[r][c] == grid[nr][nc]:
                        if dsu.union((r,c),(nr,nc)) == False:
                            return True
        return False
                
                
                        

