from math import gcd
(a, b, c, d) = map(int, input().split())
e = c * d // gcd(c, d)
cntC = b // c - (a - 1) // c
cntD = b // d - (a - 1) // d
cntE = b // e - (a - 1) // e
print(b - a - (cntC + cntD - cntE) + 1)
