from functools import lru_cache


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(maxsize=steps * arrLen)
        def num_ways(current, target, steps):
            if not 0 <= target < arrLen:
                return 0
            if steps == 0:
                return 1 if current == target else 0
            elif steps == 1:
                return 1 if abs(current - target) <= 1 else 0
            return (num_ways(current, target, steps - 1) + num_ways(current, target - 1, steps - 1) + num_ways(current, target + 1, steps - 1)) % MOD
        return num_ways(0, 0, steps)
