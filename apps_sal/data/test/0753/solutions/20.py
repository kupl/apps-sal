from fractions import Fraction
(a, b, c, d) = map(int, input().split())
if a / c <= b / d:
    res = Fraction(b * c - a * d, b * c)
else:
    res = Fraction(a * d - b * c, a * d)
print('{0}/{1}'.format(res.numerator, res.denominator))
