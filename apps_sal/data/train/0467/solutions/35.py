import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors = []
        for num in nums:
            d = set()
            for i in range(1, floor(sqrt(num) + 1)):
                if num % i == 0:
                    d.add(i)
                    d.add(num // i)
            divisors.append(d)
        result = 0
        for s in divisors:
            if len(s) == 4:
                result += sum(s)
        return result
