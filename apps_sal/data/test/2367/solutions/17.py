class Factorial:
    def __init__(self, n, mod=10**9 + 7):
        self.fac = [0] * (n + 1)
        self.ifac = [0] * (n + 1)
        self.fac[0] = 1
        self.ifac[0] = 1
        self.mod = mod
        modmod = self.mod - 2
        for i in range(n):
            self.fac[i + 1] = self.fac[i] * (i + 1) % self.mod
            self.ifac[i + 1] = self.ifac[i] * pow(i + 1, modmod, self.mod) % self.mod

    def comb(self, n, r):
        if n == 0 and r == 0:
            return 1
        if n < r or n < 0:
            return 0
        tmp = self.ifac[n - r] * self.ifac[r] % self.mod
        return tmp * self.fac[n] % self.mod

    def perm(self, n, r):
        if n == 0 and r == 0:
            return 1
        if n < r or n < 0:
            return 0
        return (self.fac[n] * self.ifac[n - r]) % self.mod


h, w, a, b = list(map(int, input().split()))
mod = 10**9 + 7
fact = Factorial(h + w + 1)
ans = 0
c, d = h - a, w - b
for i in range(b + 1, w + 1):
    d = w - i + 1
    ans = (ans + fact.comb(i + c - 2, c - 1) * fact.comb(a + d - 2, a - 1)) % mod

print(ans)
