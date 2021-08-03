class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n
        for i, value in enumerate(ranges):
            for j in range(max(i - value, 0), min(i + value, n) + 1):
                dp[j] = min(dp[j], dp[max(i - value, 0)] + 1)

        return dp[n] if dp[n] < n + 2 else -1
