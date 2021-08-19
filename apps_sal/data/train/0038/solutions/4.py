from math import *
import os
import sys
from bisect import *
from io import BytesIO
sys.setrecursionlimit(10 ** 9)
for _ in range(int(input())):
    (n, k1, k2) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) > max(b):
        print('YES')
    else:
        print('NO')
