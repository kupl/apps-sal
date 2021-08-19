from functools import lru_cache


class Solution:
    @lru_cache(None)
    def recursive(self, x, i):
        # x: steps remain, i: current position.
        if x == i:
            return 1
        count = 0
        if x > 0:
            # stay
            count += self.recursive(x - 1, i)
            # left
            if i - 1 >= 0:
                count += self.recursive(x - 1, i - 1)
            # right
            if i + 1 < self.L:
                count += self.recursive(x - 1, i + 1)
        return count % (10 ** 9 + 7)

    def numWays(self, steps: int, arrLen: int) -> int:
        self.L = arrLen
        return self.recursive(steps, 0)
