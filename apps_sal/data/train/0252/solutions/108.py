class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            L = max(0, i - ranges[i])
            R = min(n, i + ranges[i])

            for j in range(L + 1, R + 1):
                dp[j] = min(dp[j], dp[L] + 1)
        if dp[n] >= n + 2:
            return -1
        return dp[-1]
