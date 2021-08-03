from functools import lru_cache
import math


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @lru_cache(None)
        def search(i: int, d: int) -> int:
            if i == 0:
                return 0 if d == 0 else -math.inf
            ans = max(search(i - 1, d), search(i - 1, d + rods[i - 1]) + rods[i - 1])
            if rods[i - 1] <= d:
                ans = max(ans, search(i - 1, d - rods[i - 1]))
            if rods[i - 1] >= d:
                ans = max(ans, search(i - 1, rods[i - 1] - d) + rods[i - 1] - d)
            return ans

        return search(len(rods), 0)
