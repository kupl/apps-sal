N, M = map(int, input().split())

md = 1000000007
fac = [0] * (M + 1)
inv = [0] * (M + 1)
ifac = [0] * (M + 1)
inv[1] = 1
for i in range(2, M + 1):
    inv[i] = (md - (md // i) * inv[md % i] % md) % md
fac[0] = 1
ifac[0] = 1
for i in range(1, M + 1):
    fac[i] = fac[i - 1] * i % md
    ifac[i] = ifac[i - 1] * inv[i] % md


def choose(n, k):
    return fac[n] * ifac[k] * ifac[n - k] % md


def perm(m, n):
    return fac[m] * ifac[m - n] % md


ans = 0
for k in range(N + 1):
    if k % 2 == 0:
        ans += choose(N, k) * perm(M, k) * perm(M - k, N - k)**2
        ans %= md
    else:
        ans -= choose(N, k) * perm(M, k) * perm(M - k, N - k)**2
        ans %= md
print(ans)
