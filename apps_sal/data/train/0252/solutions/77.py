class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_right = [0] * (n + 1)

        for i, r in enumerate(ranges):
            max_right[max(0, i - r)] = max(max_right[max(0, i - r)], min(n, i + ranges[i]))
        dp = [float('inf')] * len(max_right)
        dp[0] = 0
        for i, x in enumerate(ranges):
            for j in range(i + 1, max_right[i] + 1):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n] if dp[n] != float('inf') else -1
