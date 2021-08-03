class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [n + 2 for _ in range(n + 1)]  # min number of water i
        dp[0] = 0
        for i, amount in enumerate(ranges):
            left = max(0, i - amount)
            right = min(n, i + amount)
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)
        return -1 if dp[n] == n + 2 else dp[n]
