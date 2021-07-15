import math
import decimal

A, B = map(str, input().split())
A = int(A)
B = decimal.Decimal(B)
print(math.floor(A*B))
