class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        f = min(target, f)
        MOD = 10 ** 9 + 7
        dp = [[None for _ in range(target + 1)] for _ in range(d + 1)]
        for i in range(1, f + 1):
            dp[1][i] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                dp[i][j] = 0
                for k in range(1, f + 1):
                    if j - k >= 1 and dp[i - 1][j - k] is not None:
                        dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= MOD
        return dp[d][target] if dp[d][target] is not None else 0
