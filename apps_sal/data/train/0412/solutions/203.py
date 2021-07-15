class Solution(object):
   def numRollsToTarget(self, d, f, t):
      mod = 1000000000+7
      dp =[[0 for i in range(t+1)] for j in range(d)]
      for i in range(d):
         for j in range(t+1):
            if i == 0:
               dp[i][j] = 1 if j>=1 and j<=f else 0
            else:
               for l in range(1,f+1):
                  if j-l>0:
                     dp[i][j]+=dp[i-1][j-l]
                     dp[i][j]%=mod
      return dp [d-1][t] % mod
ob = Solution()
print(ob.numRollsToTarget(2,6,7))
