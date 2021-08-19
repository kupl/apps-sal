
class Combination:
    def __init__(self, n_max, mod=10 ** 9 + 7):
        # O(n_max + log(mod))
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    # "n 要素" は区別できる n 要素
    # "k グループ" はちょうど k グループ

    def __call__(self, n, r):  # self.C と同じ
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nPr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[n - r] % self.mod


MOD = 10**9 + 7


def resolve():
    N, M = list(map(int, input().split()))
    cmb = Combination(5 * 10**5)

    ans = 0
    for p in range(N + 1):
        ans += (-1)**p * cmb.nCr(N, p) * cmb.nPr(M - p, N - p)
        ans %= MOD

    ans *= cmb.nPr(M, N)
    ans %= MOD

    print(ans)


def __starting_point():
    resolve()


__starting_point()
