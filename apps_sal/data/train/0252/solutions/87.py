class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for cur in range(n + 1):
            left = max(0, cur - ranges[cur] + 1)
            right = min(n, cur + ranges[cur])
            lastend = max(0, cur - ranges[cur])
            for idx in range(left, right + 1):
                dp[idx] = min(dp[idx], dp[lastend] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1
