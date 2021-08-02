#!/usr/bin/env python3
def modinv(a, mod):
    return pow(a, mod - 2, mod)


MOD = 10**9 + 7


class Factorial:
    def __init__(self, n, mod):
        # O(n + log mod)
        self.f = f = [0] * (n + 1)
        f[0] = b = 1
        for i in range(1, n + 1):
            f[i] = b = b * i % mod
        self.inv = inv = [0] * (n + 1)
        inv[n] = b = modinv(self.f[n], mod)  # pow(self.f[n], -1, mod) が Google Colab, Python ver. が低く Error
        for i in range(n, 0, -1):
            inv[i - 1] = b = b * i % mod
        self.mod = mod

    def __call__(self, n, k):  # self.C() と同じ
        return self.C(n, k)

    def factorial(self, i):
        return self.f[i]

    def ifactorial(self, i):
        return self.inv[i]

    def C(self, n, k):
        if not 0 <= k <= n: return 0
        return self.f[n] * self.inv[n - k] * self.inv[k] % self.mod

    def P(self, n, k):
        if not 0 <= k <= n: return 0
        return self.f[n] * self.inv[n - k] % self.mod

    def H(self, n, k):
        if (n == 0 and k > 0) or k < 0: return 0
        return self.f[n + k - 1] * self.inv[k] % self.mod * self.inv[n - 1] % self.mod


def factorize(n) -> list:
    b, e = 2, 0
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e:
            fct += (b, e),  # b,
        b += 1
        e = 0
    if n > 1:
        fct += (n, 1),  # n,
    return fct


n, m = map(int, input().split())
F = Factorial(n + 30, MOD)
c = 1
for _, E in factorize(m):
    c = c * F.H(n, E) % MOD
print(c)
