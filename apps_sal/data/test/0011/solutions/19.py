from math import gcd
(n, a, b, p, q) = map(int, input().split())
if p > q:
    (p, q) = (q, p)
    (a, b) = (b, a)
res = n // b * q
res += (n // a - n * gcd(a, b) // a // b) * p
print(res)
