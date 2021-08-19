class Solution:

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        return self.calcsteps(0, n)
        '\n         # this cleaner version of my approach starts at the lowest factor, then moves up when the number can no longer be cleanly divided\n         # d stands for divisor (?)\n         # both solutions run at 40ms\n         \n         ans = 0\n         d = 2\n         while n > 1:\n             while n % d == 0:\n                 ans += d\n                 n /= d\n             d += 1\n         return ans\n         '

    def isprime(self, n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def primes(self, n):
        primfac = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                primfac.append(d)
                n //= d
            d += 1
        if n > 1:
            primfac.append(n)
        return primfac

    def calcsteps(self, steps, divs):
        if self.isprime(divs):
            return divs + steps
        primes = self.primes(divs)
        return steps + sum(primes)
