from decimal import Decimal
(a, b) = input().split()
a = Decimal(a)
b = Decimal(b)
print(int(a * b))
