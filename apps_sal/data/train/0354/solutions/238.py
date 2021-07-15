from functools import lru_cache
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(None)
        def helper(rolls, side, count):
            if not rolls:
                return 1
            res = 0
            for i in range(6):
                if i != side:
                    res += helper(rolls - 1, i, 1)
                elif count + 1 <= rollMax[side]:
                    res += helper(rolls - 1, side, count + 1)
            return res
        return sum(helper(n-1, i, 1) for i in range(6)) % (10 ** 9 + 7)

