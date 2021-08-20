from decimal import Decimal
n = int(input())
i = int((-1 + Decimal(1 + 8 * (n + 1)).sqrt()) / 2)
print(n - i + 1)
