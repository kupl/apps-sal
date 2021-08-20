(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
mod = 10 ** 9 + 7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
ans = 0


def comb(n, r):
    if n >= r:
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod
    else:
        return 0


for i in range(2, N + 1):
    fac.append(fac[-1] * i % mod)
    inv.append(mod - inv[mod % i] * (mod // i) % mod)
    finv.append(finv[-1] * inv[-1] % mod)
if K == 1:
    print(0)
else:
    for (i, x) in enumerate(A):
        cnt = x * (comb(i, K - 1) - comb(N - 1 - i, K - 1)) % mod
        ans += cnt
        ans %= mod
    print(ans)
