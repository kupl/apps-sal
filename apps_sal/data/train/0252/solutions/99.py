class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        for i in range(len(ranges)):
            if i - ranges[i] <= 0:
                taps = 1
            else:
                taps = dp[i - ranges[i]] + 1

            lo = max(i - ranges[i], 0)
            hi = min(i + ranges[i], n)
            for j in range(lo, hi + 1):
                dp[j] = min(dp[j], taps)

        return dp[-1] if dp[-1] != float('inf') else -1
