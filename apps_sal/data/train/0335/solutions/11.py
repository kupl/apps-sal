class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for x in rods:
            new_dp = dp.copy()
            for d, y in dp.items():
                new_dp[d + x] = max(new_dp.get(x + d, 0), y)
                new_dp[abs(d - x)] = max(new_dp.get(abs(d - x), 0), y + min(d, x))
            dp = new_dp
        return dp[0]
