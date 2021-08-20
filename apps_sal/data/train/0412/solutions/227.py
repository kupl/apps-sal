class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        MOD = 10 ** 9 + 7
        dp[0][0] = 1
        for j in range(1, d + 1):
            for i in range(1, target + 1):
                for k in range(1, f + 1):
                    if i - k < 0:
                        break
                    dp[j][i] = (dp[j][i] + dp[j - 1][i - k]) % MOD
        return dp[d][target]
