INF = 1 << 60


class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(lambda: -INF)
        dp[0] = 0
        for a in rods:
            ndp = dp.copy()
            for (key, val) in dp.items():
                if abs(key + a) <= 5000:
                    ndp[key + a] = max(ndp[key + a], dp[key] + a)
                if abs(key - a) <= 5000:
                    ndp[key - a] = max(ndp[key - a], dp[key] + a)
            dp = ndp
        return dp[0] >> 1 if dp[0] >= 0 else 0
