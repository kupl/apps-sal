(N, M, K) = map(int, input().split())
fac = [1]
mod = 998244353
for i in range(1, N + 1):
    fac.append(fac[i - 1] * i % mod)
ifac = [None] * (N + 1)
ifac[-1] = pow(fac[N], mod - 2, mod)
for i in range(N, 0, -1):
    ifac[i - 1] = ifac[i] * i % mod
ans = 0
for k in range(K + 1):
    t = M * fac[N - 1] % mod
    t = t * ifac[N - 1 - k] % mod
    t = t * ifac[k] % mod
    t = t * pow(M - 1, N - 1 - k, mod)
    t %= mod
    ans = (ans + t) % mod
print(ans)
