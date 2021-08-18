import math
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.recurse(amount, tuple(coins))

        if result == math.inf:
            result = -1

        return result

    @lru_cache(maxsize=None)
    def recurse(self, amount: int, coins: tuple) -> int:
        if amount < 0:
            return math.inf
        elif amount == 0:
            return 0
        elif amount in coins:
            return 1
        else:
            least = math.inf
            for c in coins:
                val = self.recurse(amount - c, coins)
                least = min(least, val)

            return least + 1
