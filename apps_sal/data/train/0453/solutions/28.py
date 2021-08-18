from functools import lru_cache
import math


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 10 ** 7

        @lru_cache(None)
        def paint(i, color, k):
            if k == 0 and i == m:
                return 0
            if k < 0 or i == m:
                return MAX_COST
            if m - i < k - 1:
                return MAX_COST
            if houses[i] != 0:
                return paint(i + 1, houses[i], k - (1 if houses[i] != color else 0))
            return min((cost[i][c - 1] + paint(i + 1, c, k - (1 if c != color else 0)) for c in range(1, n + 1)))

        res = paint(0, -1, target)
        return res if res < MAX_COST else -1
