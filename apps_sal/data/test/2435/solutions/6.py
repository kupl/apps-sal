from collections import defaultdict as dd
import math
import sys
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


q = nn()

for _ in range(q):
    n, x, m = mi()
    minx = x
    maxx = x
    for i in range(m):
        l, r = mi()
        if l < minx and r >= minx:
            minx = l
        if r > maxx and l <= maxx:
            maxx = r
    print(maxx - minx + 1)
