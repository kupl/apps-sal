import math
a, b, c, d = map(int, input().split())
n, m, k = 0, 0, 0

if a % c == 0:
    n = b // c - a // c + 1
else:
    n = b // c - a // c
if a % d == 0:
    m = b // d - a // d + 1
else:
    m = b // d - a // d
e = (c * d) // math.gcd(c, d)
if a % e == 0:
    k = b // e - a // e + 1
else:
    k = b // e - a // e
k = n + m - k
print(b - a - k + 1)
