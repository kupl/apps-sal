# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


s = S()
t = S()
set_s = set(s)
set_t = set(t)
if (set_t <= set_s) is False:
    print((-1))
    return
alphabet2index = defaultdict(list)
for i, alphabet in enumerate(s):
    alphabet2index[alphabet].append(i+1)
ans = 0
pos = 0
prev_pos = 0
base = 0
n = -1
c = 0
for _t in t:
    n = s.find(_t, n+1)
    if (n == -1):
        c += 1
        n = s.find(_t)
ans = n + c*len(s) + 1
"""

    ng_flg = True
    while ng_flg:
        pos_lis = alphabet2index[_t]
        i = 0
        while len(pos_lis) > i:
            if (pos_lis[i] >= pos):
                pos = pos_lis[i]
                ans += (pos_lis[i]-prev_pos)
                # print(pos_lis[i], prev_pos, )
                prev_pos = pos
                ng_flg = False
                break
            i += 1
        else:
            prev_pos = pos - len(s)
            # print(prev_pos)
            # print('base', base)
            pos = 0
    """
print(ans)

