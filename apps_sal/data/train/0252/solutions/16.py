class Solution:

    def minTaps(self, n: int, ranges) -> int:
        dp = [0] + [float('inf')] * n
        for (i, x) in enumerate(ranges):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        print(dp)
        return dp[n] if dp[n] != float('inf') else -1
