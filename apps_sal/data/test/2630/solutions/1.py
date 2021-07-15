class Solution:
     def uniquePathsWithObstacles(self, obstacleGrid):
         """
         :type obstacleGrid: List[List[int]]
         :rtype: int
         """
         
         if not obstacleGrid or not obstacleGrid[0]:
             return 0
 
         m, n = len(obstacleGrid), len(obstacleGrid[0])
 
         # DP:
         #   dp(i, j):   no. of unique paths to obstacleGrid[i][j]
         #   bound:
         #       dp(0, 0) = 0 if obstacleGrid[0][0] == 1 else 1
         #       dp(-1, *) = 0
         #       dp(*, -1) =  0
         #   progress:
         #       dp(i, j) = | 0,             if obstacleGrid[i][j] == 1
         #                  | dp(i-1, j) + dp(i, j-1),           else
 
         dp = [0] * n
         for i in range(m):
             for j in range(n):
                 if obstacleGrid[i][j] == 1:
                     dp[j] = 0
                 else:       
                     if i == 0:
                         if j == 0:
                             dp[j] = 1
                         else:
                             dp[j] = dp[j-1]
                     else:
                         if j > 0:
                             dp[j] = dp[j] + dp[j-1]
                             
         
         return dp[n-1]
