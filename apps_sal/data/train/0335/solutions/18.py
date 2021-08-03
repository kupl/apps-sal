class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        # diff: lower length
        dp = {0: 0}
        for r in rods:
            new_dp = dp.copy()
            for d, l in dp.items():
                h = d + l
                if r + d not in new_dp:
                    new_dp[r + d] = l
                new_dp[r + d] = max(new_dp[r + d], l)
                if abs(d - r) not in new_dp:
                    new_dp[abs(d - r)] = 0
                new_dp[abs(d - r)] = max(new_dp[abs(d - r)], min(l + r, h))

            dp = new_dp
        return dp[0]
