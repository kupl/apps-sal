from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())


for i in range(int(input())):
    n = int(input())
    a = list(mdata())
    e = 0
    o = 0
    ind2 = []
    ind1 = []
    for i in range(n):
        if a[i] % 2 == 0:
            e = 1
            ind1 = i + 1
            break
        else:
            o += 1
            ind2.append(i + 1)
    if e == 1:
        print(1)
        print(ind1)
    elif o >= 2:
        print(2)
        print(*ind2[:2])
    else:
        print(-1)
