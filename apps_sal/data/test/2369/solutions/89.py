class Combination:

    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append(self.FACT[-1] * i % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append(self.FACTINV[-1] * self.INV[-1] % self.mod)

    def count(self, N, R):
        if R < 0 or N < R:
            return 0
        R = min(R, N - R)
        return self.FACT[N] * self.FACTINV[R] * self.FACTINV[N - R] % self.mod


(n, k) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
ans = 0
cmb = Combination(n, mod)
for i in range(n):
    cnt = cmb.count(i, k - 1) - cmb.count(n - i - 1, k - 1)
    ans += a[i] * cnt % mod
print(ans % mod)
