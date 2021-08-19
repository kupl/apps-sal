from fractions import Fraction
(x, y, n) = map(int, input().split(' '))
res = Fraction(x, y).limit_denominator(n)
print(res.numerator, res.denominator, sep='/')
