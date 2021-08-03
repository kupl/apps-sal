import math
a, b, c, d = map(int, input().split())
e = c * d // math.gcd(c, d)
if a % c == 0:
    p = b // c - a // c + 1
else:
    p = b // c - a // c
if a % d == 0:
    q = b // d - a // d + 1
else:
    q = b // d - a // d
if a % e == 0:
    r = b // e - a // e + 1
else:
    r = b // e - a // e
print(b - a + 1 - (p + q - r))
