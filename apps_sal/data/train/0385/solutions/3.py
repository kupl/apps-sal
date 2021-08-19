from math import sqrt, ceil


class Solution:

    def kthFactor(self, n, k):
        factors = []
        if int(sqrt(n)) == sqrt(n):
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    factors.append(i)
                    if i == int(n / i):
                        continue
                    factors.append(int(n / i))
        else:
            for i in range(1, ceil(sqrt(n))):
                if n % i == 0:
                    factors.append(i)
                    factors.append(int(n / i))
        factors.sort()
        if k > len(factors):
            return -1
        return factors[k - 1]
