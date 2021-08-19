import math


class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        self.cache = {}
        self.array_length = arrLen - 1
        return self._numWays(0, steps) % (10 ** 9 + 7)

    def _numWays(self, position, steps):
        if position > steps:
            return 0
        if (position, steps) in self.cache:
            return self.cache[position, steps]
        if steps == 1:
            if position in (-1, 0, 1):
                return 1
            else:
                return 0
        options = 0
        if position > 0:
            options += self._numWays(position - 1, steps - 1)
        if position < self.array_length:
            options += self._numWays(position + 1, steps - 1)
        options += self._numWays(position, steps - 1)
        self.cache[position, steps] = options
        return options
