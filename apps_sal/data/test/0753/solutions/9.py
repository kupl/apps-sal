from fractions import gcd, Fraction, Decimal
(a, b, c, d) = map(int, input().split())
if a / b < c / d:
    N = b * c - a * d
    D = b * c
else:
    N = a * d - b * c
    D = a * d
x = gcd(N, D)
print(N // x, end='/')
print(D // x)
