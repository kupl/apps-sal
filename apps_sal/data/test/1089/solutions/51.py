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


N, M, K = list(map(int, input().split()))
CB = Combination(10**9 + 7, 200010)

ans = 0

for d in range(N):
    ans += (((CB.comb(N * M - 2, K - 2) * (N - d) % CB.MOD) * M % CB.MOD) * M % CB.MOD) * d % CB.MOD
    ans %= CB.MOD

for d in range(M):
    ans += (((CB.comb(N * M - 2, K - 2) * (M - d) % CB.MOD) * N % CB.MOD) * N % CB.MOD) * d % CB.MOD
    ans %= CB.MOD

print(ans)
