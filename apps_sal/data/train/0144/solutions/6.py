class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 0

        return self.calcsteps(0, n)

        '''
         
         ans = 0
         d = 2
         while n > 1:
             while n % d == 0:
                 ans += d
                 n /= d
             d += 1
         return ans
         '''

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
            while (n % d) == 0:
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
