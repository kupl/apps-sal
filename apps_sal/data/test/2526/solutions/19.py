import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import bisect
import sys
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def nf():
    return float(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nb():
    return list(map(float, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


(X, Y, A, B, C) = na()
p = na()
q = na()
r = na()
p.append(inf)
q.append(inf)
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
s1 = sum(p[1:X + 1])
s2 = sum(q[1:Y + 1])
p_idx = X
q_idx = Y
ans = s1 + s2
for i in range(C):
    now_r = r[i]
    now_p = p[p_idx]
    now_q = q[q_idx]
    if now_r <= now_p and now_r <= now_q:
        break
    elif now_r > now_p and now_r > now_q:
        if now_p > now_q:
            ans = ans + now_r - now_q
            q_idx -= 1
        else:
            ans = ans + now_r - now_p
            p_idx -= 1
    elif now_r > now_p:
        ans = ans + now_r - now_p
        p_idx -= 1
    elif now_r > now_q:
        ans = ans + now_r - now_q
        q_idx -= 1
print(ans)
