from decimal import *
getcontext().prec = 28
n, m = int(input()), int(input())
lift = list(map(int, input().split()))
drop = list(map(int, input().split()))
fuel = 0
if drop[0] == 1:
    print(-1)
    return()
else:
    r = Decimal(m) / Decimal(drop[0] - 1)
    m += r
    fuel += r
lift = lift[::-1]
drop = drop[::-1]
for i in range(n - 1):
    if lift[i] == 1:
        print(-1)
        return()
    else:
        r = Decimal(m) / Decimal(lift[i] - 1)
        m += r
        fuel += r
    if drop[i] == 1:
        print(-1)
        return()
    else:
        r = Decimal(m) / Decimal(drop[i] - 1)
        m += r
        fuel += r
if lift[n - 1] == 1:
    print(-1)
    return()
else:
    r = Decimal(m) / Decimal(lift[n - 1] - 1)
    m += r
    fuel += r
print(fuel)
