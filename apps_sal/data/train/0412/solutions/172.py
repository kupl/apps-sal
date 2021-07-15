class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dp = [[0 for i in range(target+1)] for j in range(d+1)]
        
        dp[1] = [0] + [1 for i in range(f)] + [0 for i in range(target-f)]
        
        for i in range(1, d+1):
            if i==1 or i==0:
                continue
            for j in range(1, target+1):
                for k in range(1, f+1):
                    if j-k > 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % mod
                        #dp[i][j] = (dp[i][j] + dp[i-1][j-k])
        
        #print(dp)
        return dp[-1][-1]
