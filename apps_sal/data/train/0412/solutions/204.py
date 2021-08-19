class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 1000000007
        dp = [[0] * 1001 for _ in range(31)]
        mint = min(f, target)
        targetMax = d * f
        for i in range(1, mint + 1):
            dp[1][i] = 1
        for i in range(2, d + 1):
            for j in range(i, targetMax + 1):
                for k in range(1, min(j, f) + 1):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
        return dp[d][target]
