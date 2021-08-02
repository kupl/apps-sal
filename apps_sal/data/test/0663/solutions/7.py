import math
r, x, y, a, b = list(map(int, input().split()))

d = (a - x) * (a - x) + (b - y) * (b - y)

sd = d


d = pow(d, 0.5)

di = int(d)
Q = False


if(di * di == sd):
    Q = True
else:
    di = di + 1
    if(di * di == sd):
        Q = True
    else:
        di = di - 2
        if(di * di == sd):
            Q = True

if(Q):
    f = 0
    if(di % (2 * r) != 0):
        f = 1
    print(di // (2 * r) + f)
else:
    di = math.floor(d)
    print(di // (2 * r) + 1)
