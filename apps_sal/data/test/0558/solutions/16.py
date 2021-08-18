class Combination():
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    def calculate(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        return self.FACT[N] * self.FACTINV[R] * self.FACTINV[N - R] % self.mod


n, m, k = list(map(int, input().split()))
mod = 998244353

cmb = Combination(n, mod)

cnt = 0
for i in range(k + 1):
    cnt += (m * pow(m - 1, n - i - 1, mod) * cmb.calculate(n - 1, i)) % mod

print((cnt % mod))
