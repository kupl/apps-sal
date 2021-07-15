class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        
        
        # public solution ... 
        
        def dfs(pi, pj, i, j):
            visited[i][j] = True
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == grid[i][j]:
                    if visited[ni][nj]:
                        if (ni,nj) != (pi,pj):
                            return True
                    else:
                        if dfs(i, j, ni, nj):
                            return True
            return False
        
        n, m = len(grid), len(grid[0])
        if n < 2 or m < 2:
            return False
        visited = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and dfs(-1, -1, i, j):
                    return True
        return False
        
        

