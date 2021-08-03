class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        MOD = 10**9 + 7

        for i in range(d):
            for j in range(target + 1):
                for k in range(1, f + 1):
                    if j + k <= target:
                        dp[i + 1][j + k] += dp[i][j]
                        dp[i + 1][j + k] %= MOD

        return dp[d][target]
