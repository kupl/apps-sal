import sys
import itertools as it
import math as mt
import bisect as bi
import collections as cc
def I(): return list(map(int, input().split()))


for tc in range(int(input())):
    n, x = I()
    a = I()
    b = I()
    a.sort()
    b.sort(reverse=True)
    tf = 1
    for i in range(n):
        if a[i] + b[i] > x:
            tf = 0
    if tf:
        print("Yes")
    else:
        print("No")
    try:
        input()
    except:
        pass
