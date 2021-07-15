from decimal import Decimal

s, p = list(map(int, input().split()))
if Decimal(s ** 2 - 4 * p) ** Decimal(1 / 2) - int((s ** 2 - 4 * p) ** (1 / 2)) == 0:
    print("Yes")
else:
    print("No")

