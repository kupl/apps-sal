(N, M, K) = map(int, input().split())
mod = 998244353
facm = 200500
fac = [1] * facm
facinv = [1] * facm
for i in range(facm - 1):
    fac[i + 1] = fac[i] * (i + 1) % mod
    facinv[i + 1] = facinv[i] * pow(i + 1, -1, mod) % mod


def nCk(n, k):
    return fac[n] * facinv[k] * facinv[n - k] % mod


ans = 0
for i in range(K + 1):
    ans = (ans + nCk(N - 1, i) * pow(M - 1, N - i - 1, mod) * M) % mod
print(ans)
