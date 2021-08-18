import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


INF = float('inf')
mod = 10**9 + 7


def construct(BIT, arr):
    for i in range(len(arr)):
        BIT[i + 1] = arr[i]


def updateBIT(BIT, v, w):
    while v <= n:
        BIT[v] += w
        v += (v & (-v))


def getvalue(BIT, v):
    ANS = 0
    while v != 0:
        ANS += BIT[v]
        v -= (v & (-v))
    return ANS


def bisect_on_BIT(BIT, x):
    if x <= 0:
        return 0
    ANS = 0
    h = 1 << (n - 1)
    while h > 0:
        if ANS + h <= n and BIT[ANS + h] < x:
            x -= BIT[ANS + h]
            ANS += h
        h //= 2
    return ANS + 1


def update(BIT, l, r, n, val):
    updateBIT(BIT, l, val)
    updateBIT(BIT, r + 1, -val)


n = int(data())
BIT = [0] * (n + 1)
s = data()
d = dd(list)
for i in range(n):
    d[s[i]].append(i)
for i in d:
    d[i] = d[i][::-1]
ans = 0
for i in s[::-1]:
    a = d[i].pop()
    ans += getvalue(BIT, n) - getvalue(BIT, a + 1)
    updateBIT(BIT, a + 1, 1)
out(ans)
