from decimal import *
getcontext().prec = 20
a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

lo = 0
hi = 10 ** 9

hrd = 0
while abs(Decimal(lo) - Decimal(hi)) > 10 ** (-10) and hrd < 10000:
    mid = (lo + hi) / 2

    a1 = a - mid
    a2 = a + mid
    b1 = b - mid
    b2 = b + mid
    c1 = c - mid
    c2 = c + mid
    d1 = d - mid
    d2 = d + mid

    l = False
    h = False
    
    for i in [a1*d1, a1*d2, a2*d1, a2*d2]:
        for j in [b1*c1, b1*c2, b2*c1, b2*c2]:
            if i - j <= 0:
                l = True
            if i - j >= 0:
                h = True

    if l and h:
        hi = mid

    else:
        lo = mid

    hrd += 1


print(Decimal(hi))
