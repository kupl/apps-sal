import sys
import math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7


def si():
    return input()


def ii():
    return int(input())


def fi():
    return float(input())


def lstr():
    return input().split()


def lint():
    return list(map(int, input().split()))


def lintdec():
    return list(map(lambda x: int(x) - 1, input().split()))


def lnstr(n):
    return [input() for _ in range(n)]


def lnint(n):
    return [int(input()) for _ in range(n)]


def lint_list(n):
    return [lint() for _ in range(n)]


(N, M) = lint()
students = lint_list(N)
check = lint_list(M)
for (sx, sy) in students:
    ans = -1
    dist = INF
    for i in range(M):
        (cx, cy) = check[i]
        tmp = abs(cx - sx) + abs(cy - sy)
        if tmp < dist:
            dist = tmp
            ans = i + 1
    print(ans)
