class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0 for i in range(target + 1)] for i in range(d + 1)]
        for j in range(1, min(f + 1, target + 1)):
            dp[1][j] = 1
        for i in range(1, d + 1):
            for j in range(target + 1):
                for k in range(1, min(f + 1, j)):
                    dp[i][j] += dp[i - 1][j - k] % MOD
        return dp[d][target] % MOD
