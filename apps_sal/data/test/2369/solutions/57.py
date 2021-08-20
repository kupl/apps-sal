import sys
input = sys.stdin.readline
P = 10 ** 9 + 7


class MODCombination:

    def __init__(self, n, p):
        self.n = n
        self.p = p
        (self.fac, self.ifac) = self.make_fac_tables_mod_p(n, p)

    @staticmethod
    def make_fac_tables_mod_p(n, p):
        assert n >= 1
        fac = [0] * (n + 1)
        ifac = [0] * (n + 1)
        inv = [0] * (n + 1)
        fac[0] = fac[1] = 1
        ifac[0] = ifac[1] = 1
        inv[1] = 1
        for i in range(2, n + 1):
            fac[i] = fac[i - 1] * i % p
            inv[i] = p - inv[p % i] * (p // i) % p
            ifac[i] = ifac[i - 1] * inv[i] % p
        return (fac, ifac)

    def nCk(self, n, k):
        return self.fac[n] * self.ifac[n - k] % self.p * self.ifac[k] % self.p


def main():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    A.sort()
    mod_comb = MODCombination(N - 1, P)
    ans = 0
    for n in range(K - 1, N):
        max_A = A[n]
        min_A = A[-n - 1]
        ans += (max_A - min_A) * mod_comb.nCk(n, K - 1)
        ans %= P
    print(ans)


def __starting_point():
    main()


__starting_point()
