class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        newgrid = []
        for i in range(nrow*3):
            newgrid.append([0]*ncol*3)
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == '\\\\':
                    newgrid[r*3][c*3] = 1
                    newgrid[r*3+1][c*3+1] = 1
                    newgrid[r*3+2][c*3+2] = 1
                elif grid[r][c] == '/':
                    newgrid[r*3+2][c*3] = 1
                    newgrid[r*3+1][c*3+1] = 1
                    newgrid[r*3][c*3+2] = 1
        
        def countIsland(newgrid):
            count = 0
            def dfs(r,c):
                if newgrid[r][c] == 0:
                    newgrid[r][c] =1
                    if r < len(newgrid) -1 and newgrid[r+1][c] ==0:
                        dfs(r+1,c)
                    if c < len(newgrid[0]) -1 and newgrid[r][c+1] ==0:
                        dfs(r,c+1)
                    if r > 0 and newgrid[r-1][c] ==0:
                        dfs(r-1,c)
                    if c > 0 and newgrid[r][c-1] ==0:
                        dfs(r,c-1)
                    
                
            for r1 in range(len(newgrid)):
                for c1 in range(len(newgrid[0])):
                    if newgrid[r1][c1] == 0:
                        dfs(r1,c1)
                        count+=1
                    else:
                        pass
            return(count)
        
        return(countIsland(newgrid))
