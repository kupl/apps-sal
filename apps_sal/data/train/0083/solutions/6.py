from math import *
import itertools
zzz = int(input())
for zz in range(zzz):
    (x, y, a, b) = list(map(int, input().split()))
    s = y - x
    t = s / (a + b)
    if int(t) == t:
        print(int(t))
    else:
        print(-1)
