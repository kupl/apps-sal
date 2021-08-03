class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        dp = [[0] * (target + 1) for i in range(d + 1)]

        # for i in range(d+1):
        #     if
        #     dp[1][0] = 1

        dp[0][0] = 1

        for i in range(d + 1):
            for j in range(target + 1):

                for k in range(1, f + 1):
                    if j - k >= 0:

                        dp[i][j] += dp[i - 1][j - k]

        return dp[d][target] % (10 ** 9 + 7)
