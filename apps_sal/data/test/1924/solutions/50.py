class Combination:

    def __init__(self, n_max, mod=10 ** 9 + 7):
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

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod


def resolve():

    def f(r, c):
        return cmb.nCr(r + c + 2, r + 1) - 1
    MOD = 10 ** 9 + 7
    (r1, c1, r2, c2) = map(int, input().split())
    r1 -= 1
    c1 -= 1
    cmb = Combination(r2 + c2 + 5)
    ans = f(r2, c2)
    ans -= f(r1, c2)
    ans -= f(r2, c1)
    ans += f(r1, c1)
    print(ans % MOD)


def __starting_point():
    resolve()


__starting_point()
