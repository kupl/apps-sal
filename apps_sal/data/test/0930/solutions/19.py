N, K = list(map(int, input().split()))

MOD = 10**9 + 7
fac = [1] * (N + 1)
rev = [1] * (N + 1)

for i in range(1, N + 1):
    fac[i] = i * fac[i - 1] % MOD
    rev[i] = pow(fac[i], MOD - 2, MOD)


def comb(a, b): return (fac[a] * rev[a - b] * rev[b]) % MOD


ans = 0

for i in range(1 + min(N - 1, K)):
    ans += comb(N, i) * comb(N - 1, i)
ans %= MOD
print(ans)
