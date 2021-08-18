from math import *
import os
import sys
from io import BytesIO

sys.setrecursionlimit(10 ** 9)


for i in range(int(input())):
    a, b, c, r = list(map(int, input().split()))
    c1 = c - r
    c2 = c + r
    d1 = max(min(a, b), min(c1, c2))
    d2 = min(max(a, b), max(c1, c2))
    print(abs(b - a) - max(d2 - d1, 0))
