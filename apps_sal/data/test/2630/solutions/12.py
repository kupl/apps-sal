class Solution:
     def uniquePathsWithObstacles(self, obstacleGrid):
         """
         :type obstacleGrid: List[List[int]]
         :rtype: int
         """
         m, n = len(obstacleGrid), len(obstacleGrid[0])
         dp = [[1] * n for _ in range(m)]
         for i in range(m):
             dp[i][0] = 0 if obstacleGrid[i][0] == 1 else dp[i-1][0]
         for j in range(n):
             dp[0][j] = 0 if obstacleGrid[0][j] == 1 else dp[0][j-1]
         
         for i in range(1, m):
             for j in range(1, n):
                 if obstacleGrid[i][j] == 1:
                     dp[i][j] = 0
                 else:
                     dp[i][j] = dp[i-1][j] + dp[i][j-1]
         return dp[m-1][n-1]
