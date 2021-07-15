class Solution:
     def isInterleave(self, s1, s2, s3):
         """
         :type s1: str
         :type s2: str
         :type s3: str
         :rtype: bool
         """
         if len(s3) != len(s1) + len(s2): return False
         if '' in [s1, s2]: return s3 == s1+s2
         
         dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
         for i in range(len(s1)+1):
             for j in range(len(s2)+1):
                 if i == 0 and j == 0: 
                     dp[i][j] = True
                 else:
                     dp[i][j] = False
                     if j > 0: dp[i][j] |= dp[i][j-1] and s2[j-1] == s3[i+j-1]
                     if i > 0: dp[i][j] |= dp[i-1][j] and s1[i-1] == s3[i+j-1]                    
         return dp[-1][-1]
