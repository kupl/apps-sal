class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            for (d, t) in list(dp.items()):
                dp[r + d] = max(dp.get(r + d, 0), t)
                dp[abs(r - d)] = max(dp.get(abs(r - d), 0), t + min(r, d))
        return dp[0]
