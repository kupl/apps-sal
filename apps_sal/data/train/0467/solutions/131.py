import numpy as np


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        ret = 0
        for num in nums:
            divisors = set()
            N = int(np.floor(np.sqrt(num)))
            for i in range(1, N + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ret += sum(divisors)
        return ret
