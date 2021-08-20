import math
s = input().split(' ')
(n, tm, k) = (int(s[0]), int(s[1]), float(s[2]))
rq = [int(c) for c in input().split(' ')]
m = int(input())
cr = {int(c) for c in input().split(' ')}
(sr, ma) = (0, 0)
alv = []
for (c, t) in enumerate(rq):
    ma = (ma + t / tm) / k
    sr += t
    l = c - tm
    l = rq[l] if l >= 0 else 0
    sr -= l
    if c + 1 in cr:
        mr = sr / tm
        df = abs((ma - mr) / mr)
        alv.append((mr, ma, df))
for c in alv:
    print(c[0], c[1], c[2])
