class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        max_len = min(steps, arrLen)
        mod = 10 ** 9 + 7
        dp = [[0] * (max_len + 1) for _ in range(steps + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(2, steps + 1):
            for j in range(max_len):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1] + (dp[i - 1][j - 1] if j > 0 else 0)) % mod
        for r in dp:
            print(r)
        return dp[steps][0]
