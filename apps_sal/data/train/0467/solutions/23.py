from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def helper(num):
            divisors = set()
            for i in range(1, int(sqrt(num))+1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
            return sum(divisors) if len(divisors) == 4 else 0

        return sum(helper(num) for num in nums)
