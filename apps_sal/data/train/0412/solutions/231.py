class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(d+1)] for _ in range(target+1)]
        if target < d: return 0
        for i in range(2,d+1): dp[1][i] = 0
        for i in range(1,min(f+1,target+1)): dp[i][1] = 1            
        for D in range(2,d+1):
            for s in range(1,target+1):
                for k in range(1,f+1):
                    dp[s][D] += dp[s-k][D-1] if s-k >= 1 and D > 1  else 0
                    dp[s][D] = dp[s][D]%1000000007
        return dp[target][d]
