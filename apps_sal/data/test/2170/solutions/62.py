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


N, M = map(int, input().split())

MOD = 10 ** 9 + 7

F = Factorial(M + 1, MOD)

ans = 0
for k in range(N + 1):
    tmp1 = F.comb(N, k)
    tmp2 = (F.factorial(M) * F.ifactorial(M - k)) % MOD
    tmp3 = ((F.factorial(M - k) * F.ifactorial(M - N))) ** 2 % MOD
    tmp = (tmp1 * tmp2 * tmp3) % MOD
    if k % 2 == 0:
        ans += tmp
    else:
        ans -= tmp
    ans %= MOD

print(ans)
