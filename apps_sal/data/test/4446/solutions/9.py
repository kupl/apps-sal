import sys
import math
import heapq
import bisect
import re
from collections import deque
from decimal import *
from fractions import gcd


def YES_NO(flag):
    if flag:
        print('YES')
    else:
        print('NO')


def main():
    (n, a, b, k) = [int(i) for i in sys.stdin.readline().split()]
    q = [int(i) for i in sys.stdin.readline().split()]
    t = [0 for i in range(n)]
    for i in range(n):
        w = (a + b) * (q[i] % (a + b) == 0) + q[i] % (a + b)
        if w <= a:
            continue
        else:
            t[i] = (w + a - 1) // a - 1
    t = sorted(t)
    res = 0
    for i in range(n):
        if t[i] > k:
            break
        res += 1
        k -= t[i]
    print(res)


for i in range(1):
    main()
