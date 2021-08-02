from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    n = val()
    l = []
    for i in range(n): l.append(list(st()))

    ans = []
    if l[0][1] == l[1][0]:
        if l[-1][-2] == l[0][1]:
            ans.append([n - 1, n - 2])
        if l[-2][-1] == l[0][1]:
            ans.append([n - 2, n - 1])
    else:
        if l[-1][-2] == l[-2][-1]:
            if l[-1][-2] == l[0][1]:
                ans.append([0, 1])
            else:
                ans.append([1, 0])
        else:
            if l[-1][-2] == l[0][1]:
                ans.append([0, 1])
                ans.append([n - 2, n - 1])
            else:
                ans.append([1, 0])
                ans.append([n - 2, n - 1])

    print(len(ans))
    for i in ans:
        print(i[0] + 1, i[1] + 1)
