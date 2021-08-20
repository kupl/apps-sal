from functools import lru_cache


class Solution:

    @lru_cache(None)
    def helper(self, index, n, arrlen):
        if not 0 <= index < arrlen or n < 0 or index > n:
            return 0
        if index == n:
            return 1
        return (self.helper(index + 1, n - 1, arrlen) + self.helper(index - 1, n - 1, arrlen) + self.helper(index, n - 1, arrlen)) % self.MOD

    def numWays(self, steps: int, arrLen: int) -> int:
        self.MOD = 10 ** 9 + 7
        return self.helper(0, steps, arrLen)
