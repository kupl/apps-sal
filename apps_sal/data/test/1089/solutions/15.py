n, m, k = map(int, input().split())
mod = 10**9 + 7

fac = [1] * n*m
finv = [1] * n*m
inv = [1] * n*m

ans = 0
def COMinit():
    for i in range(2, n*m):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def COM(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod
COMinit()
for i in range(1, n):
    ans += (COM(n*m - 2, k-2)) * ((n-i)*i * m**2)%mod
for j in range(1, m):
    ans += (COM(n*m - 2, k-2)) * ((m-j)*j * n**2)%mod
print(ans%mod)
