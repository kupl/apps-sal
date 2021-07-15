class Solution:
     def minimumTotal(self, triangle):
         """
         :type triangle: List[List[int]]
         :rtype: int
         """
         length = len(triangle)
         dp = []
         for i in range(length):
             dp.append([])
             for j in range(len(triangle[i])):
                 dp[i].append(float('inf'))
         dp[0][0] = triangle[0][0]
         for i in range(1, length):
             dp[i][0] = dp[i-1][0] + triangle[i][0]
             dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
         
         for i in range(1, length):
             for j in range(1, len(triangle[i]) - 1):
                 dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
         return min(dp[length-1])
