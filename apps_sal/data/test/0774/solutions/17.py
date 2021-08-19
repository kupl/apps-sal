from fractions import Fraction
(a, b, c) = map(int, input().split())
print('{0.numerator}/{0.denominator}'.format(Fraction(a, b).limit_denominator(c)))
