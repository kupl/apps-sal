MOD = 10 ** 9 + 7

N, M, K = list(map(int, input().split()))

def f(x):
    return (x * (x + 1) * (x - 1)) // 6 % MOD

tmp = (N * N * f(M)) % MOD + (M * M *f(N)) % MOD

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


c = Factorial(N * M - 2, MOD).comb

tmp *= c(N * M - 2, K - 2)
tmp %= MOD

print (tmp)

