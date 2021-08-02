from decimal import *
A, B = list(map(Decimal, input().split()))
# print(A)
# print(B*100)
print((int((A * (B * 100)) // 100)))
