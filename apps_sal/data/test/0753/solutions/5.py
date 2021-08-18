from fractions import Fraction
import sys
3


a, b, c, d = list(map(int, sys.stdin.readline().strip().split()))
d2 = Fraction(d * a, c)
ans = None
if d2 <= Fraction(b):
    ans = (Fraction(b) - d2) / Fraction(b)
else:
    c2 = Fraction(c * b, d)
    ans = (Fraction(a) - c2) / Fraction(a)

if ans.denominator == 1:
    print("%d/1" % ans.numerator)
else:
    print(ans)
