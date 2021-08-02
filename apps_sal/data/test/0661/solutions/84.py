import math
import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)


def int_input():
    return list(map(int, input().split()))


m, k = int_input()
if k == 0:
    l = []
    for i in range(2 ** m):
        l.append(i)
    m = l[:]
    m.reverse()
    ans = m + l
    print((*ans))
else:
    v = 0
    l = []
    for i in range(2 ** m):
        if i != k:
            l.append(i)
            v ^= i
    m = l[:]
    m.reverse()
    ans = m + [k] + l + [k]
    if v == k: print((*ans))
    else: print((-1))
