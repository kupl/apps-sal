from functools import lru_cache
import math


class Solution:

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def paint(i, k, color):
            if k == 1 and i == m:
                return 0
            if k == 0 or i == m:
                return math.inf
            total_cost = math.inf
            if houses[i] != 0:
                if houses[i] != color:
                    k -= 1
                return paint(i + 1, k, houses[i])
            for c in range(1, n + 1):
                kk = k
                if c != color:
                    kk -= 1
                cost_ = cost[i][c - 1] + paint(i + 1, kk, c)
                total_cost = min(total_cost, cost_)
            return total_cost
        res = paint(0, target + 1, -1)
        return res if res != math.inf else -1
