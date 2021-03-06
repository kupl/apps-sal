class Factorial:

    def __init__(self, n, mod):
        self.f = f = [0] * (n + 1)
        f[0] = b = 1
        self.mod = mod
        for i in range(1, n + 1):
            f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[0] = b = pow(self.f[n], mod - 2, mod)
        for i in range(1, n + 1):
            inv[i] = b = b * (n + 1 - i) % mod
        self.inv.reverse()

    def factorial(self, i):
        return self.f[i]

    def ifactorial(self, i):
        return self.inv[i]

    def comb(self, n, k):
        return self.f[n] * self.inv[n - k] % self.mod * self.inv[k] % self.mod if n >= k else 0


M = 10 ** 9 + 7
(a, b, c, d) = map(int, input().split())
comb = Factorial(c + d + 2, M).comb


def f(r, c):
    return comb(c + r + 2, r + 1) - c - r - 2


print((f(c, d) - f(c, b - 1) - f(a - 1, d) + f(a - 1, b - 1)) % M)
