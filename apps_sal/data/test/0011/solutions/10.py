n, a, b, p, q = list(map(int, input().split()))
from fractions import gcd
ans = (n // a) * p + (n // b) * q
l = (a * b) // gcd(a, b)
ans -= (n // l) * (min(p, q))
print(ans)

