class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for j in range(d + 1)] for i in range(target + 1)]
        dp[0][0] = 1
        for i in range(1, target + 1):
            for j in range(1, d + 1):
                for k in range(1, f + 1):
                    if target - k >= 0:
                        dp[i][j] += dp[i - k][j - 1]
        return dp[target][d] % (10 ** 9 + 7)
