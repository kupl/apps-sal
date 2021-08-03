class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        dp = [n + 2 for i in range(n + 1)]
        dp[0] = 0

        for i, r in enumerate(ranges):
            for j in range(max(0, i - r), min(len(ranges), i + r + 1)):
                dp[j] = min(dp[j], dp[max(0, i - r)] + 1)

        print(dp)
        return dp[-1] if dp[-1] < n + 2 else -1
