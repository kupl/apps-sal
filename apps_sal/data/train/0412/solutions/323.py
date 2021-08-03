class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def func(d, target):
            if d == 0:
                return 1 if target == 0 else 0
            if d > target or target < 0:
                return 0
            return sum([func(d - 1, target - i) % (1e9 + 7) for i in range(1, f + 1)]) % (1e9 + 7)

        if d < 1 or f < 1 or target < 1:
            return 0
        return int(func(d, target))
