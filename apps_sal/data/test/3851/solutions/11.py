from math import gcd
(n, k) = map(int, input().split())
(a, b) = map(int, input().split())
MOD = n * k
x = int(1000000000000000.0)
y = -1
l = [b + a, 0 - a - b, a - b, b - a]
for m in range(n):
    for i in l:
        z = MOD // gcd(MOD, (k * m + i) % MOD)
        x = min(x, z)
        y = max(y, z)
print(x, y)
