class Combination:
    def __init__(self, mod, max_n):
        self.MOD = mod
        self.MAX_N = max_n

        self.f = self.factorial(self.MAX_N)
        self.f_inv = [self.inv(x) for x in self.f]

    def inv(self, x):
        return pow(x, self.MOD - 2, self.MOD)

    def factorial(self, n):
        res = [1]
        for i in range(1, n + 1):
            res.append(res[-1] * i % self.MOD)
        return res

    def comb(self, n, r):
        return (self.f[n] * self.f_inv[r] % self.MOD) * self.f_inv[n - r] % self.MOD


N, K = map(int, input().split())

CB = Combination(10**9 + 7, 10000)

for i in range(1, K + 1):
    if i > N - K + 1:
        print(0)
    else:
        print(CB.comb(N - K + 1, i) * CB.comb(K - 1, i - 1) % CB.MOD)
