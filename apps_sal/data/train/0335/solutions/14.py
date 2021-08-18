class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods)
        n = len(rods)

        dp = {0: 0}

        for num in rods:
            new_dp = dp.copy()
            for d, max_h in list(dp.items()):
                new_dp[d + num] = max(new_dp.get(d + num, 0), max_h + num)
                new_dp[abs(d - num)] = max(new_dp.get(abs(d - num), 0), max(max_h, max_h - d + num))
            dp = new_dp
        return dp[0]
