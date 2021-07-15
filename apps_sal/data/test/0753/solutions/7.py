from fractions import Fraction
from decimal import Decimal
a, b, c, d = list(map(int, input().split()))
ans = max(Fraction((a * d - b * c)/ (a * d)).limit_denominator(), Fraction((b * c - a * d) / (b * c)).limit_denominator())
if ans == 0:
    ans = '0/1'
print(ans)

