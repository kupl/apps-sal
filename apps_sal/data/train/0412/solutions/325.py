from functools import lru_cache
MOD = 10 ** 9 + 7


class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, k):
            if i == d:
                return k == 0
            return sum((dp(i + 1, k - face) for face in range(1, f + 1)))
        return dp(0, target) % MOD
