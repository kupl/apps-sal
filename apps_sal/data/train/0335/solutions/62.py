class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        for rod in rods:
            for dif, hi in list(dp.items()):
                lo = hi - dif
                ndif = abs(rod - dif)
                dp[ndif] = max(dp[ndif], hi, lo + rod)
                ndif = rod + dif
                dp[ndif] = max(dp[ndif], rod + hi)
        return dp[0]
