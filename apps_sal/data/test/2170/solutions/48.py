class Factorial:

    def __init__(self, n, mod):
        self.mod = mod
        self.fct = [0 for _ in range(n + 1)]
        self.inv = [0 for _ in range(n + 1)]
        self.fct[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.fct[i + 1] = self.fct[i] * (i + 1) % mod
        self.inv[n] = pow(self.fct[n], mod - 2, mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i + 1] * (i + 1) % mod

    def fact(self, m):
        return self.fct[m]

    def invf(self, m):
        return self.inv[m]

    def perm(self, m, k):
        if m < k:
            return 0
        return self.fct[m] * self.inv[m - k] % self.mod

    def comb(self, m, k):
        if m < k:
            return 0
        return self.fct[m] * self.inv[k] * self.inv[m - k] % self.mod


MOD = 1000000007
(N, M) = map(int, input().split())
f = Factorial(M, MOD)
res = f.perm(M, N)
for k in range(1, N + 1):
    res -= (-1) ** (k - 1) * f.comb(N, k) * f.perm(M - k, N - k)
res *= f.perm(M, N)
res %= MOD
print(res)
