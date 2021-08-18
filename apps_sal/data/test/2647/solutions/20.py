from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


h, w = readInts()
block = [input() for _ in range(h)]

allcnt = 0
for i in range(w):
    for j in range(h):
        if block[j][i] == '.':
            allcnt += 1
INF = float('inf')
AR = [[INF] * w for _ in range(h)]
dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]


def bfs():
    d = deque()
    d.append([0, 0])
    while d:
        y, x = d.popleft()
        if y == 0 and x == 0:
            AR[y][x] = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (not 0 <= ny < h) or (not 0 <= nx < w):
                continue
            if AR[ny][nx] == INF and block[ny][nx] != '
            AR[ny][nx] = AR[y][x] + 1
            d.append([ny, nx])


bfs()
if AR[h - 1][w - 1] == INF:
    print((-1))
else:
    print((allcnt - (AR[h - 1][w - 1] + 1)))
