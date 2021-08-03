from decimal import Decimal
a, b = map(Decimal, input().split())
score = a * b
score = int(score)
print(score)
