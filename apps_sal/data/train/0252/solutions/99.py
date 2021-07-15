class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # dp[i] minimum taps required to water garden[:i + 1]
        # for every ranges[i], update dp[i - ranges[i]:i + ranges[i] + 1]
        # when i - ranges[i] - 1 < 0, return 0
        # return -1 when dp[-1] is infinity
        # check if it is possible to have a hole in the middle
        dp = [float('inf')] * (n + 1)
        for i in range(len(ranges)):
            if i - ranges[i] <= 0:
                taps = 1
            else:
                taps = dp[i - ranges[i]] + 1
            
            lo = max(i - ranges[i], 0)
            hi = min(i + ranges[i], n)
            for j in range(lo, hi + 1):
                dp[j] = min(dp[j], taps)
        
        return dp[-1] if dp[-1] != float('inf') else -1

