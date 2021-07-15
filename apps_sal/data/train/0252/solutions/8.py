class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [n+2] * n + [0]
        for i in range(len(ranges)-1, -1, -1):
            x = ranges[i]
            for j in range(max(i-x, 0), min(i+x, n) + 1):
                dp[j] = min(dp[j], dp[min(i+x, n)] +1 )
                
        return dp[0] if dp[0] < n+2 else -1
