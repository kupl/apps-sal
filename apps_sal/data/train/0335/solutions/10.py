class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(lambda: -1)
        dp[0] = 0
        for x in rods:
            prevdp = dp.copy()
            for d in list(prevdp.keys()):
                dp[x + d] = max(dp[x + d], prevdp[d])
                dp[abs(x - d)] = max(dp[abs(x - d)], prevdp[d] + min(x, d))
        return dp[0]
