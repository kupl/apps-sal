from math import factorial as fac
from itertools import product


class Solution:

    def getProbability(self, balls: List[int]) -> float:

        def ways(nums):
            tmp = fac(sum(nums))
            for num in nums:
                tmp //= fac(num)
            return tmp
        half = sum(balls) // 2
        n = len(balls)
        res = 0
        stack = [list(range(ball + 1)) for ball in balls]
        comb = list(product(*stack))
        for i in range(len(comb)):
            if sum(comb[i]) == half and comb[i].count(0) == comb[-i - 1].count(0):
                res += ways(comb[i]) * ways(comb[-i - 1])
        return res / ways(balls)
