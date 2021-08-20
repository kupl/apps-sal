class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for i in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(f, j):
                    dp[i][j] = dp[i][j] + dp[i - 1][j - k]
                    k += 1
        return dp[d][target] % (10 ** 9 + 7)
