class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]
        return dp[-1][-1] % (10 ** 9 + 7)
    '\n    f = 6\n    \n     01234567\n    010000000\n    101111110\n    200123456\n         \n         \n         \n    '
