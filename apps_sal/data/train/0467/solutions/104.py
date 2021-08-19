class Solution:

    def divisors(self, n, c={}):
        if n in c:
            return c[n]
        d = []
        for i in range(1, int(sqrt(n) + 1)):
            if n % i == 0:
                d.append(i)
                j = n // i
                if j != i:
                    d.append(j)
        c.update({n: d})
        return d

    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            d = self.divisors(n)
            if len(d) == 4:
                s += sum(d)
        return s
