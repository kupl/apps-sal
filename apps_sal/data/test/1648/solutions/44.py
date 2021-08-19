
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


def resolve():
    # 青、赤それぞれの重複組み合わせ
    # K個の青いボールをi個のグループに分ける方法がK–1Ci–1通り、
    # それらを赤いボールの間に入れる方法がN-K+1Ci通り

    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split()))

    CMB = Combination(N + 1)

    for i in range(1, K + 1):
        red = CMB.nCr(N - K + 1, i) % MOD
        blue = CMB.nCr(K - 1, i - 1) % MOD
        ans = red * blue
        ans %= MOD
        print(ans)


def __starting_point():
    resolve()


__starting_point()
