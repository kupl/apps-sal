class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        dp = {0: 0}
        for rod in rods:
            for d, x in list(dp.items()):
                dp[d + rod] = max(dp.get(d + rod, 0), x)
                dp[abs(d - rod)] = max(dp.get(abs(d - rod), 0), x + min(d, rod))

        return dp[0]
