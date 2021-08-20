import decimal
x = decimal.Decimal(input())
n = x / decimal.Decimal(11)
ans = n * decimal.Decimal(2)
judge = int(ans)
if ans - judge < decimal.Decimal(0.1):
    print(int(ans))
else:
    print(int(ans) + 1)
