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
            if len(d) > 4:
                break
        if len(d) == 4:
            s = sum(d)
            c.update({n: s})
            return s
        else:
            c.update({n: 0})
            return 0

    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(self.divisors(x) for x in nums)
