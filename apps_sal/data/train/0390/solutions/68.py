import math


class Solution:
    cache = {}

    def winnerSquareGame(self, n: int) -> bool:
        if n in self.cache:
            return self.cache[n]
        for i in range(1, int(math.sqrt(n)) + 1):
            if n - i * i == 0:
                self.cache[n] = True
                return True
            if not self.winnerSquareGame(n - i * i):
                self.cache[n] = True
                return True
        self.cache[n] = False
        return False
