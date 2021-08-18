class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen < 2:
            return 1
        MAX = 10**9 + 7

        dp = [0] * arrLen
        dp[0] = 1
        dp[1] = 1

        ndp = [0] * arrLen
        for step in range(2, steps + 1):
            ndp[0] = dp[0] + dp[1]
            ndp[arrLen - 1] = dp[arrLen - 1] + dp[arrLen - 2]

            for i in range(1, min(steps, arrLen - 1)):
                ndp[i] = (dp[i] + dp[i - 1] + dp[i + 1]) % MAX

            for i in range(0, min(steps, arrLen)):
                dp[i] = ndp[i]

        return dp[0] % MAX
