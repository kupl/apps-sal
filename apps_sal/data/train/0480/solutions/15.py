class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        dp = [[0] * min(steps + 1, arrLen) for _ in range(steps + 1)]
        dp[0][0] = 1
        m, n = len(dp), len(dp[0])

        for step in range(1, steps + 1):
            for pos in range(n):
                dp[step][pos] += dp[step - 1][pos]
                if pos - 1 >= 0:
                    dp[step][pos] += dp[step - 1][pos - 1]
                if pos + 1 < n:
                    dp[step][pos] += dp[step - 1][pos + 1]
        return dp[-1][0] % (10**9 + 7)
