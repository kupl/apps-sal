N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
mod = 10**9 + 7

fac = [0] * (N + 1)
finv = [0] * (N + 1)
inv = [0] * (N + 1)

fac[0], fac[1] = 1, 1
finv[0], finv[1] = 1, 1
inv[1] = 1

for i in range(2, N + 1):
    fac[i] = (fac[i - 1] * i) % mod
    inv[i] = (- inv[mod % i] * (mod // i)) % mod
    finv[i] = finv[i - 1] * inv[i] % mod


def modcomb(n, r, mod):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * finv[r] * finv[n - r] % mod


ans = 0
ma = 0
mi = 0
for j in range(1, N + 1):

    ans += (-modcomb(N - j, K - 1, mod) + modcomb(j - 1, K - 1, mod)) * A[j - 1]
    ans %= mod
print(ans)
