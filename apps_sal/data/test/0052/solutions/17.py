from decimal import *


def is_int(d):
    return d == int(d)


getcontext().prec = 40
n = Decimal(input())
l = []
p2 = Decimal(1)
for i in range(70):
    d = 9 + 8 * n + 4 * (p2**2) - 12 * p2
    x = (3 - 2 * p2 + d.sqrt()) / 2
    if(is_int(x)):
        if(x % 2 == 1):
            l.append(p2 * x)  # l.append((p2+(x+1)/2)*x)
    p2 = p2 * 2
l.sort()
if len(l) == 0:
    print(-1)
else:
    for i in l:
        print(int(i))
