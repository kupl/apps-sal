from collections import defaultdict


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        for i in range(steps + 1):
            dp[i] = defaultdict(int)

        dp[1][1] += 1
        dp[1][0] += 1

        for i in range(2, steps + 1):
            for index in dp[i - 1].keys():
                if index + 1 < arrLen:
                    dp[i][index + 1] += dp[i - 1][index]

                if index - 1 >= 0:
                    dp[i][index - 1] += dp[i - 1][index]

                dp[i][index] += dp[i - 1][index]

        return dp[steps][0] % (10 ** 9 + 7)
