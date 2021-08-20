import math


class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        divisorSum = 0
        for num in nums:
            divisorSum += self.findDivisors(num)
        return divisorSum

    def findDivisors(self, num):
        divisors = set([1, num])
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        if len(divisors) == 4:
            return sum(list(divisors))
        return 0
