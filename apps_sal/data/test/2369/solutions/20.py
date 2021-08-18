import sys


def input(): return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7


class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  
    """

    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def make_factorial_list(self, n):
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


def solve():

    S = [0 for _ in range(N + 1)]

    comb = Combination(100001, mod)

    for i in range(N):
        S[i + 1] = S[i] + A[i]
        S[i + 1] %= mod

    ans = 0
    for i in range(K - 1, N):
        ans += (S[N] - S[i] - S[N - i]) * comb(i - 1, K - 2)
        ans %= mod

    print(ans)


def __starting_point():
    solve()


__starting_point()
