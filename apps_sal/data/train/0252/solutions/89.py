class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # dp[i] min taps to water [0, i]
        # dp[0] = 0
        dp = [0] + [n+2] * n # n+1 is possible value
        for i, v in enumerate(ranges):
            left = max(i-v, 0)
            right = min(i+v, n)
            for j in range(left, right+1):
                dp[j] = min(dp[j], dp[left]+1)
        if dp[n] < n+2:
            return dp[n]
        return -1
