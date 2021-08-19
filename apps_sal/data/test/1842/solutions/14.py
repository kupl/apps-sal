from decimal import Decimal
(a, b, c) = list(map(Decimal, input().split()))
d = (b * b - Decimal('4') * a * c).sqrt()
if a >= 0:
    print((-b + d) / (Decimal('2') * a))
    print((-b - d) / (Decimal('2') * a))
else:
    print((-b - d) / (Decimal('2') * a))
    print((-b + d) / (Decimal('2') * a))
