(n, k) = map(int, input().strip().split())
k = min(k, n - 1)
MOD = 10 ** 9 + 7


def modInv(x, m=10 ** 9 + 7):
    return pow(x, m - 2, m)


class combMod:

    def __init__(self, maxN, mod=10 ** 9 + 7):
        self.maxN = maxN
        self.mod = mod
        self.fac = [None] * (maxN + 1)
        self.ifac = [None] * (maxN + 1)

    def calc_fact(self):
        self.fac[0] = 1
        for i in range(1, self.maxN + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.ifac[-1] = modInv(self.fac[-1])
        for i in range(self.maxN, 0, -1):
            self.ifac[i - 1] = self.ifac[i] * i % self.mod

    def modnCr(self, n, r, mod=None):
        if mod is None:
            mod = self.mod
        denom = self.fac[n]
        numer = self.ifac[r] * self.ifac[n - r] % mod
        return denom * numer % mod


combMod = combMod(2 * n + 1)
combMod.calc_fact()
ans = 0
for ki in range(k + 1):
    ans += combMod.modnCr(n, ki) * combMod.modnCr(n - ki - 1 + ki, ki) % MOD
print(ans % MOD)
