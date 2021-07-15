MOD = 10 ** 9 + 7

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


N, K = map(int, input().split())

K = min(K, N - 1)

F = Factorial(N + 1, MOD)

ans = 0
for k in range(K + 1):
    tmp = F.comb(N, k) * F.factorial(N - 1) * F.ifactorial(N - 1 - k) * F.ifactorial(k)
    ans += (tmp % MOD)
    ans %= MOD

print (ans)
