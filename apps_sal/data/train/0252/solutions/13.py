class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n

        def dfs(i):
            if i == -1:
                return [0] + [n + 2] * n
            dp = dfs(i - 1)
            x = ranges[i]
            for j in range(max(i - x, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(i - x, 0)] + 1)
            return dp
        dp = dfs(n)
        return dp[n] if dp[n] < n + 2 else -1
