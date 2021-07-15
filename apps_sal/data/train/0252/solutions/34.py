class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = {i: 2*n for i in range(n+1)}
        dp[0] = 0
        for i in range(0, n+1):
            for j in range(max(0, i-ranges[i]), min(n+1, i+ranges[i]+1)):
                dp[j] = min(dp[j], dp[max(0, i-ranges[i])] + 1)
        # print(dp)
        return dp[n] if dp[n] < 2*n else -1
