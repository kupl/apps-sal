class Solution:
     def numDistinct(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: int
         """
         if len(s) < len(t):
             return 0
         dp = [0] * len(s)
         for i in range(len(s)):
             dp[i] = dp[i-1] if i > 0 else 0
             if s[i] == t[0]:
                 dp[i] += 1
                 
         for i, ti in enumerate(t[1:]):
             dp2 = [0] * len(s)
             for j in range(i+1, len(s)):
                 dp2[j] = dp2[j-1]
                 if s[j] == ti:
                     dp2[j] += dp[j-1]
             dp = dp2
         return dp[-1]

