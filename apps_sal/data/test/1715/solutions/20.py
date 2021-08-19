import heapq as hq
import itertools
import math
import collections


def ma():
    return map(int, input().split())


def lma():
    return list(map(int, input().split()))


def tma():
    return tuple(map(int, input().split()))


def ni():
    return int(input())


def yn(fl):
    return print('Yes') if fl else print('No')


mx = 3 * 10 ** 10
(a, b, q) = ma()
S = [0 for i in range(a + 2)]
T = [0 for i in range(b + 2)]
S[0] = -mx
S[a + 1] = mx
T[0] = -mx
T[b + 1] = mx
for i in range(a):
    S[i + 1] = ni()
for i in range(b):
    T[i + 1] = ni()


def bs(x, ls):
    ok = 0
    ng = len(ls) - 1
    while ng - ok > 1:
        idx = (ok + ng) // 2
        if ls[idx] < x:
            ok = idx
        else:
            ng = idx
    return ok


def solve(x):
    ids = bs(x, S)
    s1 = S[ids]
    s2 = S[ids + 1]
    idt = bs(x, T)
    t1 = T[idt]
    t2 = T[idt + 1]
    s1t1 = max(x - s1, x - t1)
    s1t2 = 2 * min(x - s1, t2 - x) + max(x - s1, t2 - x)
    s2t1 = 2 * min(s2 - x, x - t1) + max(s2 - x, x - t1)
    s2t2 = max(s2 - x, t2 - x)
    print(min(s1t1, s1t2, s2t1, s2t2))


for i in range(q):
    x = ni()
    solve(x)
