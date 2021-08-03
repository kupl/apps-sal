MOD = 10 ** 9 + 7
MAX = 5 * 10 ** 5
fac, ifac = [1] * MAX, [1] * MAX
for i in range(2, MAX):
    fac[i] = fac[i - 1] * i % MOD
ifac[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(MAX - 2, 1, -1):
    ifac[i] = ifac[i + 1] * (i + 1) % MOD
ipow2 = [1] * MAX
for i in range(1, MAX):
    ipow2[i] = ipow2[i - 1] * (MOD + 1) // 2 % MOD


def choose(n, k): return fac[n] * ifac[k] % MOD * ifac[n - k] % MOD


n, t = map(int, input().split())
a = list(map(int, input().split()))

s = 0
p = [1] + [0] * (n + 1)
k = cur = 0
for i in range(n):
    s += a[i]
    if s > t:
        break
    if s + i + 1 <= t:
        p[i + 1] = 1
        continue
    if not cur:
        k = t - s
        for j in range(k + 1):
            cur += choose(i + 1, j)
        cur %= MOD
    else:
        cur = cur * 2 - choose(i, k)
    while k > t - s:
        cur -= choose(i + 1, k)
        k -= 1
    cur %= MOD
    p[i + 1] = cur * ipow2[i + 1] % MOD

print(sum((p[i] - p[i + 1]) * i % MOD for i in range(1, n + 1)) % MOD)
