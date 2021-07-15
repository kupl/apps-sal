class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        visited = {}
        
        def dfs(x, y, u, v):
            
            if not 0 <= x < len(grid): return False
            
            if not 0 <= y < len(grid[x]): return False
            
            if grid[x][y] != grid[u][v]: return False 
            
            if (x,y) in visited:
                return True
            
            visited[(x,y)] = True
            
            if (x, y+1) != (u,v) and dfs(x, y+1,x,y):
                return True
                
            if (x-1, y) != (u,v) and dfs(x-1, y,x,y):
                return True
            
            if (x+1, y) != (u,v) and dfs(x+1, y, x, y):
                return True
                
            if (x, y-1) != (u,v) and dfs(x, y-1, x, y):
                return True
            
            return False
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and dfs(i,j,i,j):
                    return True
                
        return False
