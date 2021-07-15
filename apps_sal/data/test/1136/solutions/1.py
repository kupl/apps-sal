import math

n, m = map(int, input().split())
mod = pow(10, 9) + 7
ans = 0
if n < m:
    ans = n * (m - n) % mod
    m = n
ns = int(math.sqrt(n))
x = [0] * ns
f = 1
for i in range(ns):
    if i + 1 > m:
        f = 0
        break
    x[i] = n // (i + 1)
    ans += (n - x[i] * (i + 1))
    ans %= mod
for i in range(ns + 1, max(ns + 1, x[-1] + 1)):
    ans += n % i
    ans %= mod
if f:
    for i in range(ns - 1):
        if x[i + 1] >= m:
            continue
        c = x[i] - x[i + 1]
        ans += ((n - x[i] * (i + 1)) * c + (i + 1) * c * (c - 1) // 2)
        ans %= mod
        if x[i] >= m > x[i + 1]:
            c = x[i] - m
            ans -= ((n - x[i] * (i + 1)) * c + (i + 1) * c * (c - 1) // 2)
            ans %= mod
print(ans)
