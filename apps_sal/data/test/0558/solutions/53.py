class CombMod:
    def __init__(self, V, mod):
        self.fact = [1] * V
        self.finv = [1] * V
        for i in range(1, V):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.finv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(V - 2, 0, -1):
            self.finv[i] = self.finv[i + 1] * (i + 1) % mod
        self.mod = mod

    def comb(self, a, b):
        return self.fact[a] * self.finv[b] % mod * self.finv[a - b] % mod


N, M, K = list(map(int, input().split()))
mod = 998244353
tool = CombMod(N + 1, mod)

ans = 0
for k in range(K + 1):
    val = M * tool.comb(N - 1, k) % mod * pow(M - 1, N - 1 - k, mod) % mod
    ans = (ans + val) % mod
print(ans)

