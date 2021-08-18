class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        dp = [0] + [n + 2] * n
        for i, cur in enumerate(ranges):
            for j in range(max(0, i - cur + 1), min(n, i + cur) + 1):
                dp[j] = min(dp[j], dp[max(0, i - cur)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
