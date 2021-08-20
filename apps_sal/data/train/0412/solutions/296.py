class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f:
            return 0
        dp = [[0 for _ in range(d * f + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(i, i * f + 1):
                for t in range(1, f + 1):
                    if j - t >= i - 1 and j - t <= (i - 1) * f:
                        dp[i][j] += dp[i - 1][j - t]
        return dp[d][target] % (10 ** 9 + 7)
