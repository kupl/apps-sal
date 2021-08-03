class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen < 2:
            return 1
        MAX = 10**9 + 7

        # dp[i] is num of ways to reach position i, starting from position 0
        # if steps < i, is impossible to reach i
        dp = [0] * arrLen
        dp[0] = 1  # one step: stay
        dp[1] = 1  # one step: move right

        ndp = [0] * arrLen  # new dp array
        # dp is status for previous step
        # ndp is updated from last dp
        for step in range(2, steps + 1):
            # two boundary case at poistion 0 and arrLen-1
            ndp[0] = dp[0] + dp[1]  # stay or move from right
            ndp[arrLen - 1] = dp[arrLen - 1] + dp[arrLen - 2]  # stay or move from left

            # any other non-boundary positions
            # stay, move from left, move from right
            for i in range(1, min(steps, arrLen - 1)):
                ndp[i] = (dp[i] + dp[i - 1] + dp[i + 1]) % MAX

            # save status
            for i in range(0, min(steps, arrLen)):
                dp[i] = ndp[i]

        return dp[0] % MAX
