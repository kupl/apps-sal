from fractions import Fraction
x, y, n = map(int, input().split())
t = Fraction(x, y).limit_denominator(n)
print(str(t.numerator) + '/' + str(t.denominator))
