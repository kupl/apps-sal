import math
import bisect
from functools import reduce
from collections import defaultdict
import sys
input = sys.stdin.readline


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


MOD = 10**9 + 7
INF = inf = 10**18 + 5

s = list(input().strip())
n = len(s)
t = [[0] * 26 for i in range(2 * n)]

for i in range(n):
    t[i + n][ord(s[i]) - 97] = 1


def build():
    for i in range(n - 1, 0, -1):
        for j in range(26):
            t[i][j] = t[i << 1][j] + t[i << 1 | 1][j]


def modify(p, val):
    t[p + n][ord(s[p]) - 97] = 0
    t[p + n][ord(val) - 97] = 1
    s[p] = val
    p = p + n
    while p > 1:
        for i in range(26):
            t[p >> 1][i] = t[p][i] + t[p ^ 1][i]
        p >>= 1


def query(l, r):
    res = [0] * 26
    l += n
    r += n
    while l < r:
        if l & 1:
            for i in range(26):
                res[i] += t[l][i]
            l += 1
        if r & 1:
            r -= 1
            for i in range(26):
                res[i] += t[r][i]
        l >>= 1
        r >>= 1
    return res


build()

for q in range(inn()):
    tp, l, r = input().split()
    tp = int(tp)
    l = int(l)
    if tp == 1:
        modify(l - 1, r)
    elif tp == 2:
        r = int(r)
        res = query(l - 1, r)
        c = len([i for i in range(26) if res[i] > 0])
        print(c)
