class Solution:
     def minCut(self, s):
         """
         :type s: str
         :rtype: int
         """
         if s == s[::-1]: return 0
         for i in range(1, len(s)):
             if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                 return 1
             
             
         n = len(s)
         is_pal = [[0] * n for _ in range(n)]
         dp = [n - 1] * n
         
         for i in range(n -1, -1, -1):
             dp[i] = n - i - 1
             for j in range(i, n):
                 if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                     is_pal[i][j] = 1
                     if j == n - 1:
                         dp[i] = 0
                     elif dp[j + 1] + 1 < dp[i]:
                         dp[i] = dp[j + 1] + 1
                         
         return dp[0]

