class Combination:

    def __init__(self, n, mod=10 ** 9 + 7):
        self.mod = mod
        self.fac = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.invfac = [1] * (n + 1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.invfac[i] = self.invfac[i + 1] * (i + 1) % self.mod

    def combination(self, n, r):
        ans = self.fac[n] * self.invfac[r] % self.mod * self.invfac[n - r] % self.mod
        if n >= r:
            return ans
        else:
            return 0

    def factorial(self, i):
        return self.fac[i]

    def invfactorial(self, i):
        return self.invfac[i]


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    (n, m, k) = map(int, input().split())
    mod = 998244353
    c = Combination(n, mod)
    ans = 0
    mex = [0] * (k + 1)
    mex[0] = pow(m - 1, n - k - 1, mod)
    for i in range(1, k + 1):
        mex[i] = mex[i - 1] * (m - 1) % mod
    mex = mex[::-1]
    for i in range(k + 1):
        ans += c.combination(n - 1, i) * mex[i]
        ans %= mod
    ans *= m
    ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
