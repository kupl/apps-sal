import math
import re


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


n, k = ria()
ar = ria()
if k == 1:
    print(min(ar))
    return
if k == 2:
    print(max(min(ar[1:]),min(ar[:-1]), ar[0], ar[-1]))
    return

print(max(ar))
