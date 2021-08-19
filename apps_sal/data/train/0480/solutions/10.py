class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps // 2 + 1)
        dp = [0] * arrLen
        dp[0] = 1
        for i in range(steps):
            dp = [(dp[x - 1] if x >= 1 else 0) + dp[x] + (dp[x + 1] if x + 1 < arrLen else 0) for x in range(arrLen)]
        return dp[0] % (10 ** 9 + 7)
