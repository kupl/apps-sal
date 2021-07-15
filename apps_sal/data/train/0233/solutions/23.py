class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m, ans = [[[0, 0, 0, 0] for j in range(n)] for i in range(n)], 0
        
        def dfs(i, j, k):
            if 0 <= i < n and 0 <= j < n and not m[i][j][k]:
                if grid[i][j] == '/':
                    if 1 <= k <= 2:
                        m[i][j][1] = m[i][j][2] = ans
                        dfs(i, j+1, 3)
                        dfs(i+1, j, 0)
                    else:
                        m[i][j][0] = m[i][j][3] = ans 
                        dfs(i-1, j, 2)
                        dfs(i, j-1, 1)
                elif grid[i][j] == '\\\\':
                    if k <= 1:
                        m[i][j][0] = m[i][j][1] = ans
                        dfs(i-1, j, 2)
                        dfs(i, j+1, 3)
                    else:
                        m[i][j][2] = m[i][j][3] = ans 
                        dfs(i+1, j, 0)
                        dfs(i, j-1, 1)
                else:
                    m[i][j][0] = m[i][j][1] = m[i][j][2] = m[i][j][3] = ans 
                    dfs(i-1, j, 2)
                    dfs(i, j-1, 1)
                    dfs(i+1, j, 0)
                    dfs(i, j+1, 3)
                    
        
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not m[i][j][k]:
                        ans += 1
                        dfs(i, j, k)
                        
        return ans 

