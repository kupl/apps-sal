import math

n, a, b, p, q = [int(x) for x in input().split(' ')]

g = int(a * b / math.gcd(a, b))

if p > q: l = q
else: l = p
print((n // a) * p + (n // b) * q - (n // g) * l)
