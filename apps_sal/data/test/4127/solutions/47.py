import decimal
a, b = input().split()
x = decimal.Decimal(a)
y = decimal.Decimal(b)
ans = int(x * y)
print(ans)
