#!/usr/bin/env python
n, k = list(map(int, input().split()))
mod = 10**9 + 7

d = [-1 for _ in range(k + 1)]
d[k] = 1

for i in range(k - 1, 0, -1):
    d[i] = pow(k // i, n, mod)
    j = 2 * i
    while j <= k:
        d[i] -= d[j]
        j += i

#print('d =', d)
ans = 0
for i in range(1, k + 1):
    ans += (i * d[i]) % mod
print((ans % mod))
