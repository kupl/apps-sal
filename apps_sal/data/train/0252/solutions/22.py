class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(max(0, i - ranges[i]), (min(n, i + ranges[i])) + 1):
                dp[j] = min(dp[j], 1 + dp[max(0, i - ranges[i])])

        if(dp[n] == sys.maxsize):
            return -1
        return dp[n]
