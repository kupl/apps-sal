class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        for i in range(steps + 1):
            dp[i] = collections.defaultdict(int)

        # dp[i][j] stores the number of ways to reach index j using i steps
        dp[1][1] += 1  # move right
        dp[1][0] += 1  # stay
        # cannot move left at this moment, as index j must satisfy 0 <= sums < arrLen

        for i in range(2, steps + 1):
            # index is where we are after the first i-1 steps
            for index in dp[i - 1].keys():
                if index + 1 < arrLen:  # move right
                    dp[i][index + 1] += dp[i - 1][index]

                if index - 1 >= 0:  # move left
                    dp[i][index - 1] += dp[i - 1][index]

                dp[i][index] += dp[i - 1][index]  # stay

        return dp[steps][0] % (10 ** 9 + 7)
