from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations, groupby
import sys
import bisect
import string
import math
import time
import random


def S_():
    return input()


def LS():
    return [i for i in input().split()]


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return [int(i) for i in input().split()]


def LI_():
    return [int(i) - 1 for i in input().split()]


def NI(n):
    return [int(input()) for i in range(n)]


def NI_(n):
    return [int(input()) - 1 for i in range(n)]


def StoI():
    return [ord(i) - 97 for i in input()]


def ItoS(nn):
    return chr(nn + 97)


def LtoS(ls):
    return ''.join([chr(i + 97) for i in ls])


def GI(V, E, Directed=False, index=0):
    org_inp = []
    g = [[] for i in range(n)]
    for i in range(E):
        inp = LI()
        org_inp.append(inp)
        if index == 0:
            inp[0] -= 1
            inp[1] -= 1
        if len(inp) == 2:
            (a, b) = inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp) == 3:
            (a, b, c) = inp
            aa = (inp[0], inp[2])
            bb = (inp[1], inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return (g, org_inp)


def bit_combination(k, n=2):
    rt = []
    for tb in range(n ** k):
        s = [tb // n ** bt % n for bt in range(k)]
        rt += [s]
    return rt


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
mo = 10 ** 9 + 7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase
ts = time.time()
sys.setrecursionlimit(10 ** 5)


def input():
    return sys.stdin.readline().rstrip()


def ran_input():
    import random
    n = random.randint(4, 16)
    (rmin, rmax) = (1, 10)
    a = [random.randint(rmin, rmax) for _ in range(n)]
    return (n, a)


show_flg = False
show_flg = True
ans = 0
t = I()
for _ in range(t):
    (h, w) = LI()
    ans = []
    t = []
    ng = False
    rs = [[inf, -inf] for i in range(26)]
    cs = [[inf, -inf] for i in range(26)]
    for i in range(h):
        s = input()
        t.append(s)
        for j in range(w):
            if s[j] != '.':
                k = ord(s[j]) - 97
                rs[k][0] = min(rs[k][0], i + 1)
                rs[k][1] = max(rs[k][1], i + 1)
                cs[k][0] = min(cs[k][0], j + 1)
                cs[k][1] = max(cs[k][1], j + 1)
    ll = -1
    for i in range(26):
        if rs[i][0] != inf:
            ll = i
    if ll == -1:
        print('YES')
        print(0)
        continue
    for i in range(ll + 1)[::-1]:
        if (rs[i][0] != inf and rs[i][0] != rs[i][1]) and (cs[i][0] != inf and cs[i][0] != cs[i][1]):
            ng = True
            break
        elif rs[i][0] == inf:
            ans.append(lsn)
        else:
            lsn = [rs[i][0], cs[i][0], rs[i][1], cs[i][1]]
            ans.append(lsn)
            for r in range(rs[i][0], rs[i][1] + 1):
                for c in range(cs[i][0], cs[i][1] + 1):
                    if ord(t[r - 1][c - 1]) - 97 < i:
                        ng = True
    if ng:
        print('NO')
        continue
    else:
        print('YES')
        print(len(ans))
        for i in ans[::-1]:
            print(*i)
