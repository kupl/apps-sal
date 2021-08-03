class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for r in rods:
            for diff, y in list(dp.items()):
                dp[diff + r] = max(dp.get(diff + r, 0), y)
                if diff - r >= 0:
                    dp[diff - r] = max(dp.get(diff - r, 0), y + r)
                if r - diff >= 0:
                    dp[r - diff] = max(dp.get(r - diff, 0), y + diff)
                # dp[abs(diff - r)] = max(dp.get(abs(diff - r), 0), y + min(diff, r))
        return dp[0]
