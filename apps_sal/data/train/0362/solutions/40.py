from functools import lru_cache
from operator import iconcat
from functools import reduce

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        hat_ids = list(set(reduce(iconcat, hats, [])))
        n = len(hats)
        m = len(hat_ids)
        k = (1 << n) - 1

        @lru_cache(None)
        def dp(i, used):
            if i == m:
                return 1 if used == k else 0

            total = dp(i + 1, used)
            for p in range(n):
                if used & (1 << p) == 0 and hat_ids[i] in hats[p]:
                    total += dp(i + 1, used | (1 << p))
            return total % MOD

        return dp(0, 0)



