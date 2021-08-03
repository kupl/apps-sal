class Combination:
    """
    SIZEが10^6程度以下の二項係数を何回も呼び出したいときに使う
    使い方:
    comb = Combination(SIZE, MOD)
    comb(10, 3) => 120
    """

    def __init__(self, N, MOD=10 ** 9 + 7):
        self.MOD = MOD
        self.fact, self.inv = self._make_factorial_list(N)

    def __call__(self, n, k):
        if k < 0 or k > n:
            return 0
        res = self.fact[n] * self.inv[k] % self.MOD
        res = res * self.inv[n - k] % self.MOD
        return res

    def _make_factorial_list(self, N):
        fact = [1] * (N + 1)
        inv = [1] * (N + 1)
        MOD = self.MOD
        for i in range(1, N + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        inv[N] = pow(fact[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            inv[i - 1] = (inv[i] * i) % MOD
        return fact, inv


def __starting_point():
    r1, c1, r2, c2 = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    comb = Combination(2 * 10 ** 6 + 10, mod)

    def f(r, c):
        return comb(r + c + 2, r + 1)

    CD = (f(r2, c2) - f(r2, c1 - 1) + mod) % mod
    C = (f(r1 - 1, c2) - f(r1 - 1, c1 - 1) + mod) % mod
    ans = (CD - C + mod) % mod
    print(ans)


__starting_point()
