class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n
        for i, v in enumerate(ranges):
            left = max(i - v, 0)
            right = min(i + v, n)
            for j in range(left + 1, right + 1):
                dp[j] = min(dp[j], dp[max(0, i - v)] + 1)
        if dp[n] < n + 2:
            return dp[n]
        return -1
