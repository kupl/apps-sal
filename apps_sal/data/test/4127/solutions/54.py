import decimal
A, B = map(decimal.Decimal, input().split())
num = A * B
print(int(num) // 1)
