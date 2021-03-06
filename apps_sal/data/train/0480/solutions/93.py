class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        needed = min(steps + 1, arrLen)
        dp = [0 for i in range(needed + 1)]
        new_dp = dp.copy()
        dp[0] = 1
        for step in range(1, steps + 1):
            for pos in range(min(step + 1, arrLen)):
                new_dp[pos] = dp[pos] + dp[pos - 1] + dp[pos + 1]
            (dp, new_dp) = (new_dp, dp)
        return dp[0] % (10 ** 9 + 7)
        needed = min(arrLen, steps + 1)
        dp = [0 for i in range(needed + 1)]
        dp[0] = 1
        next_dp = dp.copy()
        for step in range(1, steps + 1):
            for pos in range(min(step + 1, arrLen)):
                next_dp[pos] = dp[pos - 1] + dp[pos] + dp[pos + 1]
            print((step, next_dp, dp))
            (dp, next_dp) = (next_dp, dp)
        return dp[0] % (10 ** 9 + 7)
