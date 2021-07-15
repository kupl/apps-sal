class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        rows = [0]*m
        cols = [0]*n        
        for r, row in enumerate(grid):
            for c, server in enumerate(row):
                if (server==1):
                    rows[r]+=1
                    cols[c]+=1
        
        ans = 0
        for r, row in enumerate(grid):
            for c, server in enumerate(row):
                if (server==1 and (rows[r]>1 or cols[c]>1)):
                    ans += 1
                    
        return ans

