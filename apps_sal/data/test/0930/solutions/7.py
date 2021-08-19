class Combination:

    def __init__(self, size, mod=10 ** 9 + 7):
        self.size = size + 2
        self.mod = mod
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size
        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % self.mod
            self.inv[i] = -self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % self.mod

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % self.mod

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % self.mod) % self.mod

    def nhr(self, n, r):
        return self.ncr(n + r - 1, n - 1)

    def factN(self, n):
        if n < 0:
            return 0
        return self.fact[n]


(N, K) = list(map(int, input().split()))
K = min(K, N)
MOD = 10 ** 9 + 7
comb = Combination(N + 100)
ans = 0
for k in range(K + 1):
    ans += comb.ncr(N, k) * comb.nhr(N - k, k)
    ans %= MOD
print(ans)
