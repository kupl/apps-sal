N, M, K = list(map(int, input().split()))
MOD = 998244353
MAX_N = 10**6
fac = [0] * (MAX_N)
fac_inv = [0] * (MAX_N)
fac[0] = 1
for i in range(MAX_N - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD
fac_inv[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(MAX_N - 2, -1, -1):
    fac_inv[i] = fac_inv[i + 1] * (i + 1) % MOD


def nCk(n, k):
    return fac[n] * fac_inv[k] % MOD * fac_inv[n - k] % MOD


ans = 0
for k in range(K + 1):
    # temp = M*nCk(N-1, k)*pow(M-1, N-K-1, MOD) % MOD
    temp = (M * nCk(N - 1, k)) % MOD * pow(M - 1, N - k - 1, MOD) % MOD
    ans += temp
    ans %= MOD
print(ans)
