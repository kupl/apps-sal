class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        F = [i for i in range(m * n)]
        def find(x):
            if x == F[x]:
                return x
            else:
                F[x] = find(F[x])
                return F[x]
            
        for i in range(n):
            for j in range(m):
                if i > 0 and grid[i-1][j] == grid[i][j]:
                    f1 = find((i-1)*m+j)
                    f2 = find((i)*m+j)
                    if f1 == f2:
                        return True
                    F[f1] = f2
                if j > 0 and grid[i][j-1] == grid[i][j]:
                    f1 = find((i)*m+j-1)
                    f2 = find((i)*m+j)
                    if f1 == f2:
                        return True
                    F[f1] = f2
        return False

