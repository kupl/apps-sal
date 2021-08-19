from fractions import Fraction
(x, y, n) = map(int, input().split())
ans = Fraction(x, y).limit_denominator(n)
print(ans.numerator, '/', ans.denominator, sep='')
