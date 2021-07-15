class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            divisors = self.getDivisors(n)
            if len(divisors) == 4:
                res += sum(divisors)
        return res

    def getDivisors(self, n):
        divisors = set()
        for i in range(1, n):
            if i ** 2 > n:
                break
            if n % i == 0:
                divisors.add(i)
                divisors.add(n//i)
            if len(divisors) > 4:
                break
        return divisors
