class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            dp2 = dp.copy()
            for d in list(dp.keys()):
                dp2[d + r] = max(dp2.get(d + r, 0), dp[d])
                dp2[abs(d - r)] = max(dp2.get(abs(d - r), 0), dp[d] + min(d, r))
            dp = dp2
        return dp[0]
