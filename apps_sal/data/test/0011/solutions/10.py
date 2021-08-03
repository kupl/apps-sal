from fractions import gcd
n, a, b, p, q = list(map(int, input().split()))
ans = (n // a) * p + (n // b) * q
l = (a * b) // gcd(a, b)
ans -= (n // l) * (min(p, q))
print(ans)
