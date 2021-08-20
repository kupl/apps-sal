from itertools import accumulate as ac
from bisect import bisect_left as bsl
from bisect import bisect as bs
from math import factorial as f
from collections import Counter as cc
from bisect import *
from itertools import *
from heapq import *
from math import *
from sys import *
from queue import *
from collections import *
from re import *
from string import *
(z, zz) = (input, lambda: list(map(int, z().split())))


def zzz():
    return [int(i) for i in stdin.readline().split()]


(szz, graph, mod, szzz) = (lambda: sorted(zz()), {}, 10 ** 9 + 7, lambda: sorted(zzz()))


def lcd(xnum1, xnum2):
    return xnum1 * xnum2 // gcd(xnum1, xnum2)


def prime(x):
    p = ceil(x ** 0.5) + 1
    for i in range(2, p):
        if x % i == 0 and x != 2 or x == 0:
            return 0
    return 1


def dfs(u, visit, graph):
    visit[u] = True
    for i in graph[u]:
        if not visit[i]:
            dfs(i, visit, graph)


'\n\n\n\n'
num = 1
num = int(z())
for _ in range(num):
    (a, b, c) = szzz()
    print(c)
