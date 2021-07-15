r1, c1, r2, c2 = map(int, input().split())
MOD = 10 **9 + 7

ans = 0

class Factorial:
    def __init__(self, n, mod):
        self.f = [1]
        self.mod = mod
        for j in range(1, n + 1):
            self.f.append(self.f[-1] * j % mod)
        self.i = [pow(self.f[-1], mod - 2, mod)]
        for j in range(n, 0, -1):
            self.i.append(self.i[-1] * j % mod)
        self.i.reverse()
    def factorial(self, j):
        return self.f[j]
    def ifactorial(self, j):
        return self.i[j]
    def comb(self, n, k):
        return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod if n >= k else 0

F = Factorial(r2 + c2 + 3, MOD)

ans = F.comb(c1 + r1, c1) - F.comb(c1 + r2 + 1, c1) - F.comb(c2 + r1 + 1, c2 + 1) + F.comb(c2 + r2 + 2, c2 + 1)

print (ans % MOD)
