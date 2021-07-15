class Solution:
     def minPathSum(self, grid):
         """
         :type grid: List[List[int]]
         :rtype: int
         """
         if not grid:
             return 0
         row_count = len(grid)
         col_count = len(grid[0])
         dp = [[0 for _ in range(col_count)] for _ in range(row_count)]
         dp[0][0] = grid[0][0]
         if row_count == col_count and col_count == 1:
             return dp[-1][-1]
         for row in range(row_count):
             for col in range(col_count):
                 if row == 0 and col >= 1:
                     dp[row][col] = dp[row][col-1] + grid[row][col]
                 elif col == 0 and row >= 1:
                     dp[row][col] = dp[row-1][col] + grid[row][col]
                 else:
                     dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
         return dp[-1][-1]
