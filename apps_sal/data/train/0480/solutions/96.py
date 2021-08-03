class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        v = min(steps, arrLen)
        dp = [0] * v
        dp[0] = 1
        temp = [0] * v
        for _ in range(steps):
            left = 0
            for idx, val in enumerate(dp):
                temp = val
                right = 0 if idx == len(dp) - 1 else dp[idx + 1]
                dp[idx] += left + right
                left = temp

        return dp[0] % (10**9 + 7)
