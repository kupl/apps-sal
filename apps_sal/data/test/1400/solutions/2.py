MOD = 10 ** 9 + 7
MAX = 5 * 10 ** 5
fac, ifac, ipow2 = [1] * MAX, [1] * MAX, [1] * MAX
for i in range(1, MAX):
    fac[i] = fac[i - 1] * i % MOD
    ifac[i] = pow(fac[i], MOD - 2,MOD)
    ipow2[i] = ipow2[i - 1] * (MOD + 1) // 2 % MOD

choose = lambda n, k: fac[n] * ifac[k] % MOD * ifac[n - k] % MOD

n, t = map(int, input().split())
a = list(map(int, input().split()))

s = 0
p = [1] + [0] * (n + 1)
k = cur = 0
for i in range(n):
    s += a[i]
    if s > t: break
    if s + i + 1 <= t:
        p[i + 1] = 1
        continue
    newk = t - s
    cur = cur * 2 - choose(i, k) if cur else sum(choose(i + 1, j) for j in range(newk + 1)) % MOD
    if newk < k:
        cur -= sum(choose(i + 1, x) for x in range(k, newk, -1))
    cur %= MOD
    p[i + 1] = cur * ipow2[i + 1] % MOD
    k = newk

print(sum((p[i] - p[i + 1]) * i % MOD for i in range(1, n + 1)) % MOD)
