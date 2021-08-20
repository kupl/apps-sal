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
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n - r] % self.mod

    def permutation(self, n, r):
        return self.factorial(n) * self.invfactorial(n - r) % self.mod

    def factorial(self, i):
        return self.fac[i]

    def invfactorial(self, i):
        return self.invfac[i]


def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    (n, m) = map(int, input().split())
    c = Combination(m)
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(n + 1):
        tmp = c.combination(n, i) * pow(-1, i % 2) * c.permutation(m, i) % mod
        tmp *= c.permutation(m - i, n - i) ** 2
        tmp %= mod
        ans += tmp
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
