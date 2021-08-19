class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for (idx, r) in enumerate(ranges):
            for j in range(max(idx - r + 1, 0), min(idx + r, n) + 1):
                dp[j] = min(dp[j], dp[max(0, idx - r)] + 1)
        return dp[n] if dp[n] < float('inf') else -1
