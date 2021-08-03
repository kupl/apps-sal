U = 2 * 10 ** 5
mod = 10 ** 9 + 7


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
    N, K = map(int, input().split())
    comb = Combination(U + 5, mod)

    ans = 1
    for i in range(1, min(K + 1, N)):
        vacant = comb(N, i)
        person = comb(N - 1, i)
        ans = (ans + vacant * person % mod) % mod
    print(ans)


__starting_point()
