class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = int(10 ** 9 + 7)
        dp = [[0 for i in range(d + 1)] for j in range(target + 1)]
        dp[0][0] = 1
        for i in range(1, target + 1):
            for j in range(1, d + 1):
                for k in range(1, f + 1):
                    if i >= k:
                        dp[i][j] += dp[i - k][j - 1] % mod
                    dp[i][j] = dp[i][j] % mod
        return dp[-1][-1] % mod
