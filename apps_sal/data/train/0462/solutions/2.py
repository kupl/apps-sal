class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                
                if grid[i][j] == 1:
                    d1[i]+=1
                    d2[j]+=1
                    
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (d1[i]>1 or d2[j]>1):
                    c+=1
                    
        return c
                
                    

