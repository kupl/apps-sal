import random
import math
import heapq
import itertools
import bisect
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from copy import deepcopy


def examA():
    C = [SI()for _ in range(3)]
    ans = C[0][0] + C[1][1] + C[2][2]
    print(ans)
    return


def examB():
    N, M = LI()
    P = [0] * N
    S = [LSI()for _ in range(M)]
    pena = 0
    ac = set()
    for p, s in S:
        p = int(p) - 1
        if s == "WA":
            P[p] += 1
        else:
            if p in ac:
                continue
            ac.add(p)
            pena += P[p]

    print(len(ac), pena)
    return


def examC():
    W, H, N = LI()
    lx, rx, ly, ry = 0, W, 0, H
    A = [LI()for _ in range(N)]
    for x, y, a in A:
        if a == 1:
            lx = max(lx, x)
        elif a == 2:
            rx = min(rx, x)
        elif a == 3:
            ly = max(ly, y)
        elif a == 4:
            ry = min(ry, y)
    ans = max(0, rx - lx) * max(0, ry - ly)
    print(ans)
    return


def examD():
    N, H = LI()
    B = [0] * N
    maxa = 0
    ans = 0
    for i in range(N):
        a, B[i] = LI()
        if a > maxa:
            maxa = a
    B.sort(reverse=True)
    for b in B:
        if b < maxa:
            break
        H -= b
        ans += 1
        if H <= 0:
            print(ans)
            return
    ans += -(-H // maxa)
    print(ans)
    return


def examE():
    A, B = LI()
    ans = [["#"] * 100 for _ in range(50)] + [["."] * 100 for _ in range(50)]
    i = 0
    j = 0
    for _ in range(A - 1):
        ans[i][j] = "."
        j += 2
        if j >= 100:
            j = 0
            i += 2
    i = 0
    j = 0
    for _ in range(B - 1):
        ans[99 - i][j] = "#"
        j += 2
        if j >= 100:
            j = 0
            i += 2
    print(100, 100)
    for v in ans:
        print("".join(map(str, v)))
    return


def examF():
    ans = 0
    print(ans)
    return


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int, readline().split()))
def LSI(): return list(map(str, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()


nonlocal mod, mod2, inf, alphabet, _ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)


def __starting_point():
    examE()


"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""
__starting_point()
