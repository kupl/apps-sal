from itertools import accumulate


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


def resolve():
    n, k = list(map(int, input().split()))
    a = sorted(map(int, input().split()))
    mod = 10**9 + 7

    fact = Factorial(n + 1)
    lll = [fact.comb(i, k - 1) for i in range(k - 1, n)]

    ans = 0
    for i in range(n - k + 1):
        ans = (ans + (a[-i - 1] - a[i]) * lll[-i - 1]) % mod
    print(ans)


def __starting_point():
    resolve()


__starting_point()
