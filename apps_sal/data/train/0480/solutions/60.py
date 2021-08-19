MODULO = 10 ** 9 + 7


class DP:

    def __init__(self, arrLen: int):
        self._len = arrLen
        self._cache = {}

    def get(self, index, steps):
        if (index, steps) in self._cache:
            return self._cache[index, steps]
        result = self._get_uncached(index, steps)
        self._cache[index, steps] = result
        return result

    def _get_uncached(self, index, steps):
        if index < 0 or index >= self._len:
            return 0
        if steps == 0 and index == 0:
            return 1
        elif steps == 0:
            return 0
        return (self.get(index - 1, steps - 1) + self.get(index, steps - 1) + self.get(index + 1, steps - 1)) % MODULO


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        dp = DP(arrLen)
        return dp.get(0, steps)
