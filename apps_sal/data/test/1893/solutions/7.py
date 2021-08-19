from decimal import Decimal
(n, t) = list(map(int, input().split()))
print(Decimal(n) * pow(Decimal('1.000000011'), int(t)))
