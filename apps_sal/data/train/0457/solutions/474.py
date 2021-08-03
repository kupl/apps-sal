from functools import lru_cache
from math import inf


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def cc(i, amount):
            if amount == 0:
                return 0
            elif i < 0 or amount < 0:
                return inf
            else:
                incl, excl = cc(i - 1, amount), cc(i, amount - coins[i]) + 1
                return min(max(incl, 0), max(excl, 0))

        result = cc(len(coins) - 1, amount)
        return result if result < inf else -1
