from functools import lru_cache
import math


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def paint(i, color, k):
            if k == 0 and i == m:
                return 0
            if k < 0 or i == m:
                return math.inf
            total_cost = math.inf
            if houses[i] != 0:
                return paint(i + 1, houses[i], k - (1 if houses[i] != color else 0))
            for c in range(1, n + 1):
                cost_ = cost[i][c - 1] + paint(i + 1, c, k - (1 if c != color else 0))
                total_cost = min(total_cost, cost_)
            return total_cost
        res = paint(0, -1, target)
        return res if res != math.inf else -1
