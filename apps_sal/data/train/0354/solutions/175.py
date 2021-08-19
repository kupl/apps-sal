from functools import lru_cache


class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        @lru_cache(None)
        def roll(val, cons, left):
            if left == 0:
                return 1
            ans = sum([roll(nval, 1, left - 1) for nval in range(6) if nval != val])
            if cons < rollMax[val]:
                ans += roll(val, cons + 1, left - 1)
            return ans
        return roll(0, 0, n) % (10 ** 9 + 7)
