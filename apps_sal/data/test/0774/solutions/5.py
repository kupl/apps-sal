from fractions import Fraction as F

x, y, n = map(int, input().split())
a = F(x, y).limit_denominator(n)
print(a.numerator, '/', a.denominator, sep='')
