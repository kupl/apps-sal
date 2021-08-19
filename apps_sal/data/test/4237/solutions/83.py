from math import gcd
(a, b, c, d) = map(int, input().split())
lcm = c * d // gcd(c, d)
a -= 1
p = b // c - a // c
q = b // d - a // d
r = b // lcm - a // lcm
a += 1
print(b - a + 1 - (p + q - r))
