import sys
import math


def inint():
    return int(sys.stdin.readline())


def inintm():
    return map(int, sys.stdin.readline().split())


def inintl():
    return list(inintm())


def instrm():
    return map(str, sys.stdin.readline().split())


def instrl():
    return list(instrm())


(w, h, n) = inintm()
ll = [0, 0]
rh = [w, h]
for i in range(n):
    (x, y, a) = inintm()
    if a == 1:
        ll[0] = max(ll[0], x)
    elif a == 2:
        rh[0] = min(rh[0], x)
    elif a == 3:
        ll[1] = max(ll[1], y)
    else:
        rh[1] = min(rh[1], y)
if rh[0] - ll[0] < 0 or rh[1] - ll[1] < 0:
    print(0)
else:
    print((rh[0] - ll[0]) * (rh[1] - ll[1]))
