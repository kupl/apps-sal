import sys
sys.setrecursionlimit(250000)
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        def valid(x, y):
            if x < m and x >= 0 and y < n and y >= 0:
                return True
            else:
                return False
        
        def dfs(x, y, parent_x, parent_y):
            visit[x][y] = 1
            
            for d in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                new_x = x + d[0]
                new_y = y + d[1]
                if valid(new_x, new_y) and grid[new_x][new_y] == grid[x][y] and (not (parent_x == new_x and parent_y == new_y)):
                    if visit[new_x][new_y] == 1:
                        return True
                    else:
                        cur = dfs(new_x, new_y, x, y)
                        if cur:
                            return True
            
            return False
        
        visit = [[0 for _ in range(n)] for _ in range(m)]
        
        res = False
        
        for i in range(m):
            if res:
                return True
            
            for j in range(n):
                if visit[i][j] == 0:
                    res = dfs(i, j, -1, -1)
                
                if res:
                    return True
        
        return False
