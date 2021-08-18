
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
    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split()))

    CMB = Combination(N + 1)

    for i in range(1, K + 1):
        if i > N - K + 1:
            print((0))
        else:
            ans = CMB.nCr(N - K + 1, N - K - i + 1)
            ans = ans * CMB.nCr(K - 1, K - i)
            ans %= MOD
            print(ans)


def __starting_point():
    resolve()


__starting_point()
