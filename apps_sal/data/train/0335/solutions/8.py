from functools import lru_cache
from collections import defaultdict


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        dp = defaultdict(int)
        dp[0] = 0
        for x in rods:
            for d, y in list(dp.copy().items()):
                dp[d + x] = max(dp[d + x], y)
                dp[abs(d - x)] = max(dp[abs(d - x)], y + min(d, x))
        return dp[0]
