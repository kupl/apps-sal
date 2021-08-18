class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        if n < 1 or ranges is None:
            return -1
        dp = [None] * len(ranges)
        for i in range(len(dp)):
            l = max(0, i - ranges[i])
            r = min(len(dp) - 1, i + ranges[i])
            for j in range(l, r + 1):
                if dp[j] is None:
                    dp[j] = l
                else:
                    dp[j] = min(dp[j], l)
            if dp[-1] == 0:
                return 1
        i = len(dp) - 1
        c = 0
        while i > 0 and dp[i] is not None and dp[i] != i:
            i = dp[i]
            c += 1
        return c if i == 0 else -1
