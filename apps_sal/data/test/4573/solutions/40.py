from decimal import Decimal

n = int(input())
x = list(map(int, input().split()))

y = x.copy()

y.sort()

m1 = y[n // 2]
m2 = y[n // 2 - 1]
m = Decimal(m1 + m2) / Decimal(2)
#print(m1, m2)

for z in x:
    if z <= m:
        print(m1)
    else:
        print(m2)
