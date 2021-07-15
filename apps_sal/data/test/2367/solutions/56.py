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
    H, W, A, B = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    comb = Combination(2 * 10 ** 5 + 10, mod)

    ans = 0
    x = H - A
    y = B + 1
    while x > 0 and y <= W:
        path1 = comb(x + y - 2, x - 1)
        path2 = comb(H - x + W - y, H - x)
        ans = (ans + path1*path2) % mod
        x -= 1
        y += 1

    print(ans)

__starting_point()
