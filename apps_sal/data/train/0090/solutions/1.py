import sys
import math as mt
import collections as cc
import sys
import itertools as it
input = sys.stdin.readline


def I():
    return list(map(int, input().split()))


for tc in range(int(input())):
    (n,) = I()
    ar = I()
    l = I()
    s = []
    ll = l.copy()
    loc = cc.defaultdict(int)
    for i in range(n):
        if l[i] == 0:
            s.append(ar[i])
            loc[i] = -10 ** 6
        else:
            loc[i] = ar[i]
    s.sort(reverse=True)
    j = 0
    for i in range(n):
        if l[i] == 0:
            l[i] = s[j]
            j += 1
        else:
            l[i] = ar[i]
    print(*l)
