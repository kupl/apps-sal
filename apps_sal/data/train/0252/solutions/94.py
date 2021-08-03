class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        for i, tmp in enumerate(ranges):
            left = max(0, i - tmp)
            right = min(n, i + tmp)

            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)
        return dp[n] if dp[n] < sys.maxsize else -1
