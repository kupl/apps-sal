class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [n + 2] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            for j in range(start, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)
        if dp[n] == n + 2:
            return -1
        return dp[n]
