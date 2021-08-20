from itertools import accumulate
from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop, heapify
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    l = [0] + li3()
    x = val()
    n = len(l) - 1
    ans = [None] * (n + 1)
    flag = 0
    for i in range(1, n + 1):
        if l[i] == 1:
            if i > x and (ans[i - x] == 1 or ans[i - x] == None):
                ans[i - x] = 1
            elif i + x <= n:
                ans[i + x] = 1
            else:
                flag = 1
                break
        elif (i <= x or (ans[i - x] == None or ans[i - x] == 0)) and (i + x > n or ans[i + x] == None):
            if i > x:
                ans[i - x] = 0
            if i + x <= n:
                ans[i + x] = 0
        else:
            flag = 1
            break
    for i in range(1, n + 1):
        if ans[i] == None:
            ans[i] = 1
    if flag:
        print(-1)
    else:
        print(*ans[1:n + 1], sep='')
