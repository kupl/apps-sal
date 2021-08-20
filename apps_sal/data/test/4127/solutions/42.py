from decimal import Decimal, ROUND_DOWN
(a, b) = map(lambda x: Decimal(x), input().split())
print(Decimal(a * b).quantize(Decimal('1.'), rounding=ROUND_DOWN))
