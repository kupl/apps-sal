from decimal import Decimal, ROUND_CEILING
n = Decimal(input())
print(((Decimal(2) * n + Decimal(3) - (Decimal(8) * n + Decimal(9)).sqrt()) / Decimal(2)).to_integral_value(ROUND_CEILING))
