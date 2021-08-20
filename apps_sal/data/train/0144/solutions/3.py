class Solution:

    def minSteps(self, n):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        ret = 0
        for p in primes:
            while not n % p:
                n /= p
                ret += p
        return int(ret + n * (n > 1))
