class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [sys.maxsize] * (n + 1)
        for i in range(n + 1):
            if ranges[i] == 0:
                continue
            l = max(0, i - ranges[i])
            r = min(n, i + ranges[i])
            for j in range(l, r + 1):
                if l == 0:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], 1 + dp[l])
        if dp[n] == sys.maxsize:
            return -1
        return dp[n]
