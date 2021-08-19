class Solution:

    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2
        import math

        def isPrime(n):
            lm = int(math.floor(math.sqrt(n)))
            for i in range(2, lm + 1):
                if n % i == 0:
                    return False
            return True

        def odd(n):
            t = n
            n = n // 10
            mul = 1
            new = 0
            while n:
                new = new * 10 + n % 10
                mul = mul * 10
                n = n // 10
            return t * mul + new

        def even(n):
            t = n
            mul = 1
            new = 0
            while n:
                new = new * 10 + n % 10
                mul = mul * 10
                n = n // 10
            return t * mul + new
        o = 1
        e = 1
        while True:
            opal = odd(o)
            epal = even(e)
            if opal < epal:
                if opal >= N and isPrime(opal):
                    return opal
                o += 1
            else:
                if epal >= N and isPrime(epal):
                    return epal
                e += 1
