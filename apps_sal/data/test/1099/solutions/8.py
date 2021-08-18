import sys
from collections import defaultdict as dd
from collections import deque
from fractions import Fraction as f
from copy import *
from bisect import *
from heapq import *
from math import *
from itertools import permutations


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1

if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')


def li():
    return [int(x) for x in input().split()]


def fli():
    return [float(x) for x in input().split()]


def gi():
    return [x for x in input().split()]


def fi():
    return int(input())


def si():
    return list(input().rstrip())


def mi():
    return map(int, input().split())


def gh():
    sys.stdout.flush()


def graph(n, m):
    for i in range(m):
        x, y = mi()
        a[x].append(y)
        a[y].append(x)


def bo(i):
    return ord(i) - ord('a')


tt = 1


while tt > 0:
    tt -= 1
    n = fi()
    a = [[] for i in range(n + 1)]
    for i in range(n - 1):
        x, y = mi()
        a[x].append(y)
        a[y].append(x)
    dis = [0 for i in range(n + 1)]
    q = deque()
    q.append(1)
    vis = [0 for i in range(n + 1)]
    vis[1] = 1
    while len(q):
        z = q.popleft()
        for j in a[z]:
            if vis[j] == 0:
                vis[j] = 1
                dis[j] = dis[z] ^ 1
                q.append(j)
    print(min(dis[1:].count(0), dis[1:].count(1)) - 1)
