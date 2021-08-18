# /usr/bin/env python

n, m = list(map(int, input().split()))
MOD = int(1e9) + 7
fac = [-1 for _ in range(100001)]
fac[1] = 1

for i in range(1, 100000):
    fac[i + 1] = ((i + 1) * fac[i]) % MOD

if abs(n - m) > 1:
    print((0))
    return

ans = 0
if n == m:
    ans = (fac[n] * fac[m] * 2) % MOD
else:
    ans = (fac[n] * fac[m]) % MOD

print(ans)
