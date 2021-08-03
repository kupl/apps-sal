from math import sqrt


class Solution:
    def primePalindrome(self, N: int) -> int:
        def subgen(start, upper, odd):
            start = int(start)
            for i in range(start, upper):
                if odd:
                    yield int(str(i) + str(i)[:-1][::-1])
                else:
                    yield int(str(i) + str(i)[::-1])

        def is_prime(n):
            factors = []
            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    factors.extend([i, n // i])
                    if len(factors) > 2:
                        return False
            return len(factors) <= 2

        def generator(N):
            if N <= 10:
                for i in range(2, 10):
                    if is_prime(i):
                        yield i
            if N <= 11:
                yield 11
            if N <= 1000:
                for i in subgen('10', 100, True):
                    if is_prime(i):
                        yield i
            if N <= 10000:
                for i in subgen('10', 100, False):
                    if is_prime(i):
                        yield i
            if N <= 100000:
                for i in subgen('100', 1000, True):
                    if is_prime(i):
                        yield i
            if N <= 1000000:
                for i in subgen('100', 1000, False):
                    if is_prime(i):
                        yield i
            if N <= 10000000:
                for i in subgen('1000', 10000, True):
                    if is_prime(i):
                        yield i
            if N <= 100000000:
                for i in subgen('1000', 10000, False):
                    if is_prime(i):
                        yield i
            if N <= 1000000000:
                for i in subgen('10000', 20000, True):
                    if is_prime(i):
                        yield i

        for g in generator(N):
            if g >= N:
                return g
