class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10 ** 9 + 7
        if target > d * f:
            return 0

        dp = [[0 for j in range(target + 1)] for i in range(d + 1)]
        for j in range(1, min(f, target) + 1):
            dp[1][j] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(max(1, j - f), j):
                    dp[i][j] += dp[i - 1][k]
        return dp[d][target] % mod
