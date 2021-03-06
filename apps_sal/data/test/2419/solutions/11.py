from heapq import heappush, heappop, heapify
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
import math
import time


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return [int(i) for i in input().split()]


def LI_():
    return [int(i) - 1 for i in input().split()]


def StoI():
    return [ord(i) - 97 + 10 for i in input()]


def ItoS(nn):
    return chr(nn + 97)


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


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
mo = 10 ** 9 + 7
inf = float('inf')
l_alp = string.ascii_lowercase
u_alp = string.ascii_uppercase


def input():
    return sys.stdin.readline().rstrip()


show_flg = False
show_flg = True
t = I()
for _ in range(t):
    ans = 0
    (a, b) = LI()
    if a > b:
        (a, b) = (b, a)
    if a == b:
        print(0)
        continue
    nb = max(int((2 * (b - a)) ** 0.5) - 3, 0)
    for i in range(nb, nb * 2 + 100):
        if a + i * (i + 1) // 2 >= b and (a + i * (i + 1) // 2 - b) % 2 == 0:
            print(i)
            break
