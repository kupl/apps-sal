class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        g = [[0 for _ in range(n*3)] for _ in range(n*3)]
        
        def dfs(i, j):
            if 0 <= i < (n*3) and 0 <= j < (n*3) and g[i][j] == 0:
                g[i][j] = 1
                for k in [1, -1]:
                    dfs(i+k, j)
                    dfs(i, j+k)
                    
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i*3][(j*3) + 2] = 1
                    g[(i*3) + 1][(j*3) + 1] = 1
                    g[(i*3) + 2][j*3] = 1
                elif grid[i][j] == '\\\\':
                    g[i*3][j*3] = 1
                    g[(i*3) + 1][(j*3) + 1] = 1
                    g[(i*3) + 2][(j*3) + 2] = 1
        res = 0
        for i in range(n*3):
            for j in range(n*3):
                if g[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res
