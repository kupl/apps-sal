from decimal import *

getcontext().prec = 50
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

answer = None

for k in range(1 << 4):
    le = Decimal(0)
    rg = Decimal(10 ** 11)

    def f(t):
        fi = a
        if k & 1:
            fi += t
        else:
            fi -= t

        fi *= (d + t if k & (1 << 1) else d - t)

        se = (b + t if k & (1 << 2) else b - t)
        se *= (c + t if k & (1 << 3) else c - t)

        return abs(fi - se)

    for i in range(200):
        m1 = le + (rg - le) / Decimal(3)
        m2 = rg - (rg - le) / Decimal(3)

        if f(m1) > f(m2):
            le = m1
        else:
            rg = m2

    if f(le) < 1e-8:
        if answer == None:
            answer = le
        else:
            answer = min(answer, le)

print(answer)

