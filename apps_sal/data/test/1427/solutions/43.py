import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


mod = 10 ** 9 + 7


class Factorize(object):

    def __init__(self, maxnum):
        self.primes = self.__smallest_prime_factors(maxnum)

    def factorize_list(self, n):
        fct = []
        while n != 1:
            fct.append(self.primes[n])
            n //= self.primes[n]
        return fct

    def factorize_dict(self, n):
        fct = defaultdict(lambda: 0)
        while n != 1:
            fct[self.primes[n]] += 1
            n //= self.primes[n]
        return fct

    def __smallest_prime_factors(self, n):
        prime = list(range(n + 1))
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] != i:
                continue
            for j in range(i * 2, n + 1, i):
                prime[j] = min(prime[j], i)
        return prime


def divmod(x, mod=10 ** 9 + 7):
    return pow(x, mod - 2, mod)


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    fct = Factorize(max(A))
    lcm_dict = defaultdict(lambda: 0)
    for i in range(N):
        d = fct.factorize_dict(A[i])
        for (k, v) in list(d.items()):
            lcm_dict[k] = max(lcm_dict[k], v)
    lcm = 1
    for (k, v) in list(lcm_dict.items()):
        lcm *= k ** v
        lcm %= mod
    ans = 0
    for i in range(N):
        ans += divmod(A[i])
        ans %= mod
    ans *= lcm
    ans %= mod
    print(ans)


def __starting_point():
    solve()


__starting_point()
