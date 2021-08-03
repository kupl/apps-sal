from math import pi, sin
from decimal import Decimal

n, r = map(int, input().split())
alpha = Decimal(pi) / Decimal(n)
a = Decimal(sin(alpha))
R = Decimal((r * a) / (1 - a))
print(R)
