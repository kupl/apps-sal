import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class Eratosthenes:
    def __init__(self, n):
        self.n = n
        self.min_factor = [-1] * (n + 1)
        self.min_factor[0], self.min_factor[1] = 0, 1

    def get_primes(self):
        primes = []
        is_prime = [True] * (self.n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, self.n + 1):
            if not is_prime[i]:
                continue
            primes.append(i)
            self.min_factor[i] = i
            for j in range(i * 2, self.n + 1, i):
                is_prime[j] = False
                if self.min_factor[j] == -1:
                    self.min_factor[j] = i
        return primes

    def prime_factorization(self, n):
        res = []
        while n != 1:
            prime = self.min_factor[n]
            exp = 0
            while self.min_factor[n] == prime:
                exp += 1
                n //= prime
            res.append([prime, exp])
        return res


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    MAX_A = max(A) + 1

    er = Eratosthenes(MAX_A)
    er.get_primes()
    num = [0] * MAX_A
    for i in range(n):
        pf = er.prime_factorization(A[i])
        for p, ex in pf:
            num[p] = max(num[p], ex)

    LCM = 1
    for v in range(2, MAX_A):
        LCM *= pow(v, num[v], mod)
        LCM %= mod

    res = 0
    for a in A:
        res += LCM * pow(a, mod - 2, mod)
        res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
