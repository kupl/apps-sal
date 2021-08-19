class Combination:
    def __init__(self, n_max, mod=10**9 + 7):
        # O(n_max + log(mod))
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

# 同じ色が隣り合う確率...1/M
# 隣り合う箇所...N-1
# ちょうどn箇所隣り合う確率...(N-1)Cn * (1/M)^n * ((M-1)/M)^(N-1-n)
# 全パターン...M^N


N, M, K = list(map(int, input().split()))
mod = 998244353
comb = Combination(202020, mod)
ans = 0
for n in range(0, K + 1):
    ans += comb(N - 1, n) * pow(M - 1, N - 1 - n, mod) % mod
ans = ans * M % mod
print(ans)
