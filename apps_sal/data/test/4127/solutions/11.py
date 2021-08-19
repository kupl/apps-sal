import decimal
(a, b) = input().split()
a = int(a)
b = decimal.Decimal(b)
c = b * 100
x = a * int(c)
print(x // 100)
