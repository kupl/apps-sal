class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for x in rods:
            temp = dp.copy()
            for (diff, height) in list(dp.items()):
                temp[diff + x] = max(temp.get(diff + x, 0), height)
                temp[abs(x - diff)] = max(temp.get(abs(diff - x), 0), height + min(diff, x))
            dp = temp.copy()
        return dp[0]
