import math as mt
n, d = map(int, input().split())
print(mt.ceil(n / (2 * d + 1)))
