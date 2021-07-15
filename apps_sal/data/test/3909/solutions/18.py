import math, decimal

n = int(input())
k = 0
while n % 3**k == 0:
    k += 1

D = decimal.Decimal
print(math.ceil(D(n) / D(3**k)))
