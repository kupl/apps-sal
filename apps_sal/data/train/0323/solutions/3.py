class Solution:
     def isInterleave(self, s1, s2, s3):
         """
         :type s1: str
         :type s2: str
         :type s3: str
         :rtype: bool
         """
         if len(s1) + len(s2) != len(s3):
             return False
         
         m, n = len(s1) + 1, len(s2) + 1
         dp = [[False] * n for _ in range(m)]
         
         dp[0][0] = True
         for row in range(1, m):
             dp[row][0] = dp[row - 1][0] and s1[row - 1] == s3[row - 1]
         
         for col in range(1, n):
             dp[0][col] = dp[0][col - 1] and s2[col - 1] == s3[col - 1]
         
         for row in range(1, m):
             for col in range(1, n):
                 # print(row, col)
                 # print(s1[row - 1])
                 # print(s2[col - 1])
                 # print(s3[row + col - 1])
                 dp[row][col] = (dp[row - 1][col] and s1[row - 1] == s3[row + col - 1]) \
                                or (dp[row][col - 1] and s2[col - 1] == s3[row + col - 1])
         
         # print(dp)
         
         return dp[-1][-1]

