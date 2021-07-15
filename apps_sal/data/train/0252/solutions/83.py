class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inf = 1 << 50
        prev = collections.defaultdict(lambda: inf)
        for i, r in enumerate(ranges):
            prev[min(i+r, n)] = min(prev[min(i+r, n)],max(i-r,0))
 
        dp = [inf] * (n + 1)
        dp[0] = 0
 
        for x in range(n+1):
            for y in range(prev[x], x):
                dp[x] = min(dp[y] + 1, dp[x])
 
        res = dp[n]
        if res >= inf:
            return -1
 
        return res
