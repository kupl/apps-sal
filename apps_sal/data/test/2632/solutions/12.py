class Solution:
     def minPathSum(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         m = len(grid)
         n = len(grid[0])
         if m == 0 or n == 0: return 0
         
         memory = [[0 for _ in range(n)] for _ in range(m)]
         
         def minSum(grid,x,y,n,m):
             if x==0 and y==0: return grid[0][0]
             if x<0 or y<0: return float("inf")
             if memory[y][x] > 0: return memory[y][x]
             memory[y][x] = grid[y][x] + min(minSum(grid,x-1,y,n,m),minSum(grid,x,y-1,n,m))
             return memory[y][x]
             
         return minSum(grid,n-1,m-1,n,m)
     
         

