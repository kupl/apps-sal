class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n
        for i, v in enumerate(ranges):
            for j in range(max(0, i - v + 1), min(n, i + v) + 1):
                dp[j] = min(dp[j], dp[max(0, i - v)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
