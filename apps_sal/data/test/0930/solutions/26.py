import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
mod = 10 ** 9 + 7
(n, k) = list(map(int, input().split()))
fac = [1] * (n + 1)
inv = [1] * (n + 1)
for i in range(1, n + 1):
    fac[i] = fac[i - 1] * i % mod
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n, 0, -1):
    inv[i - 1] = inv[i] * i % mod


def cmb(n, r):
    if r < 1:
        return 1
    return fac[n] * inv[r] % mod * inv[n - r] % mod


ans = 0
k = min(k, n - 1)
for i in range(k + 1):
    ans += cmb(n, i) * cmb(n - 1, i) % mod
print(ans % mod)
