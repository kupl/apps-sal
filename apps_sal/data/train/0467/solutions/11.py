class Solution:
    def divisors(self, n):
        for i in range(1, int(sqrt(n) + 1)):
            if n % i == 0:
                yield i
                j = n // i
                if j != i:
                    yield j

    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            l = list(self.divisors(n))
            if len(l) == 4:
                s += sum(l)
        return s
