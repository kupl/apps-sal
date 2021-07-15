class Solution:
     def calculateMinimumHP(self, dungeon):
         """
         :type dungeon: List[List[int]]
         :rtype: int
         """
         m=len( dungeon)  
         n=len( dungeon[0])
         
         dp=[[float('inf') for _ in range(n+1)] for _ in range(m+1)]
         dp[m][n-1]=1
         dp[m-1][n]=1
         
         for i in range(m-1,-1,-1):
             for j in range(n-1,-1,-1):
                 
                 need =min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                 if need <=0:
                     need=1
                 dp[i][j]=need 
         return dp[0][0]        
