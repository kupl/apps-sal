import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


class Combination():
    def __init__(self, n, mod=10**9 + 7):
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
    n, k = mi()
    mod = 10**9 + 7
    c = Combination(n)
    for i in range(k):
        if n - k < i:
            print(0)
            continue
        tmp = c.combination(n - k + 1, i + 1)
        tmp *= c.combination(k - 1, i)
        tmp %= mod
        print(tmp)


def __starting_point():
    main()


__starting_point()
