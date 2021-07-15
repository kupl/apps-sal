class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n = min(steps+1, arrLen)
        dp = [0]*n
        dp[0] = 1
        MOD = 10**9+7
        
        for _ in range(steps):
            ndp = [0]*n
            
            for i in range(n):
                if i==0:
                    ndp[i] = (dp[i]+dp[i+1])%MOD
                elif i==n-1:
                    ndp[i] = (dp[i-1]+dp[i])%MOD
                else:
                    ndp[i] = (dp[i-1]+dp[i]+dp[i+1])%MOD
            
            dp = ndp
            
        return dp[0]
