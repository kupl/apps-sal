class Solution:
     def numDistinct(self, s, t):
         """
         :type s: str
         :type t: str
         :rtype: int
         """
         setOft=set(t)
         news=""
         for ch in s:
             if ch in setOft:
                 news+=ch
         dp=[[1 for i in range(len(news)+1)] for j in range(len(t)+1)]
         for j in range(1,len(t)+1):
             dp[j][0]=0
 
         for i in range(len(t)):
             for j in range(len(news)):
                 if t[i]==news[j]:
                     dp[i+1][j+1]=dp[i][j]+dp[i+1][j]
                 else:
                     dp[i+1][j+1]=dp[i+1][j]
         return dp[len(t)][len(news)]

