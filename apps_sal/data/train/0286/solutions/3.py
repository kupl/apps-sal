from math import comb, prod
from itertools import accumulate


class Solution:

    def getCombinations(self, balls, l, r, d):
        if not balls:
            return d == 0
        if abs(d) > len(balls):
            return 0
        (x, count) = (balls.pop(), 0)
        for i in range(x + 1):
            if l >= i and r >= x - i:
                count += comb(l, i) * comb(r, x - i) * self.getCombinations(balls.copy(), l - i, r - (x - i), d - (i == 0) + (i == x))
        return count

    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls)
        total = prod((comb(n, x) for (n, x) in zip(accumulate(balls), balls)))
        count = self.getCombinations(balls, n // 2, n // 2, 0)
        return count / total
