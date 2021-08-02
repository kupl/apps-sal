# from decimal import *
# getcontext().prec=16
# from math import sqrt
# from scipy.special import binom
# from collections import defaultdict
# from math import sin,pi,sqrt
from math import sqrt, hypot


def dist(a, b, c):
    return abs((c[1] - a[1]) * b[0] - (c[0] - a[0]) * b[1] + c[0] * a[1] - c[1] * a[0]) / hypot(c[0] - a[0], c[1] - a[1]) / 2


n = int(input())
liste = [list(map(int, input().split(" "))) for _ in range(n)]

d = -1
for i in range(n):
    if i == n - 1:
        a, b, c = liste[n - 2], liste[n - 1], liste[0]
    else:
        a, b, c = liste[i - 1], liste[i], liste[i + 1]
    if d != -1:
        d = min(d, dist(a, b, c))
    else:
        d = dist(a, b, c)

print(d)
