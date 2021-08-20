import sys
from functools import reduce
MOD = 1000000007


def solve(N: int):
    from itertools import chain
    from collections import Counter
    from functools import reduce
    pu = PrimeUtil(N + 1)
    c = Counter(chain.from_iterable((pu.factor_iter(i) for i in range(2, N + 1))))
    return reduce(lambda a, b: a * (b + 1) % MOD, list(c.values()), 1)


class PrimeUtil:

    def __init__(self, size):
        self.size = size
        self._init_table()

    def _init_table(self):
        from itertools import takewhile
        self._is_prime = [True] * self.size
        self._is_prime[0] = False
        self._is_prime[1] = False
        for i in takewhile(lambda x: x * x <= self.size, list(range(self.size))):
            if not self._is_prime[i]:
                continue
            for j in range(i + i, self.size, i):
                self._is_prime[j] = False

    def prime_iter(self):
        return [x for x in range(self.size) if self._is_prime[x]]

    def primes(self):
        return tuple(self.prime_iter())

    def factor_iter(self, n):
        from itertools import takewhile
        m = n
        for p in self.prime_iter():
            while m % p == 0:
                yield p
                m //= p
            if m == 1:
                return

    def factors(self, n):
        return tuple(self.factor_iter(n))


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    print(solve(N))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
