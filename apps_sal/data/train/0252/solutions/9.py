class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n

        def dfs(i):
            x = ranges[i]
            for j in range(max(i - x, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(i - x, 0)] + 1)
        for i in range(len(ranges)):
            dfs(i)
        return dp[n] if dp[n] < n + 2 else -1
