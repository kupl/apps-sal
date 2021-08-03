import math


class Solution:

    def s_factors_if_len_4(self, n, d):
        s = set()
        for i in range(1, math.floor(n**0.5) + 1):
            if n % i == 0:
                s.add(i)
                s.add(n // i)
        if len(s) == 4:
            d[n] = sum(s)
        else:
            d[n] = 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        d = {}
        sol = 0
        for n in nums:
            if n not in d.keys():
                self.s_factors_if_len_4(n, d)
            sol += d[n]
        return sol
