class Solution:
     def minPathSum(self, grid): 
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         xx=len(grid)-1
         yy=len(grid[0])-1
         gridv=[[0 for j in range(len(grid[0]))] for i in range(len(grid))]
         gridv[xx][yy]=grid[xx][yy]
         for i in range(xx,-1,-1):
             for j in range(yy,-1,-1):
                 if i==xx:
                     if j==yy:
                          gridv[i][j]=grid[xx][yy]
                     else:
                          gridv[i][j]=grid[i][j]+gridv[i][j+1]
                 elif j==yy:
                     if i==xx:
                          gridv[i][j]=grid[xx][yy]
                     else:
                          gridv[i][j]=grid[i][j]+gridv[i+1][j]
                 else:            
                     gridv[i][j]=min(gridv[i+1][j]+grid[i][j],gridv[i][j+1]+grid[i][j])
         print(grid)
         print(gridv)
         return gridv[0][0]
     
         """"
         if(len(grid)==1 or len(grid[0])==1):
             return sum(sum(grid,[]))
         if
         return grid[0][0]+min(self.minPathSum(grid[1:],x,y+1),self.minPathSum([grids[1:] for grids in grid],x+1,y))
         """""
