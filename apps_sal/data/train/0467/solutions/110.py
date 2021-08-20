from collections import defaultdict
from math import ceil


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def getSumOfDivisors(n):
            divisors = set()
            for i in range(1, ceil(n ** 0.5) + 1):
                if n % i == 0:
                    divisors.update({i, n // i})
                if len(divisors) > 4:
                    return 0
            return sum(divisors) if len(divisors) == 4 else 0
        return sum(map(getSumOfDivisors, nums))
