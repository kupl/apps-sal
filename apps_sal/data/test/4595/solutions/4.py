import sys
import math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10 ** 9)


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


def lint_dec():
    return list(map(lambda x: int(x) - 1, input().split()))


def lnstr(n):
    return [input() for _ in range(n)]


def lnint(n):
    return [int(input()) for _ in range(n)]


def lint_list(n):
    return [lint() for _ in range(n)]


t = si()
n = len(t)
for s in range(n):
    if t[s] == 'A':
        break
for e in range(n - 1, -1, -1):
    if t[e] == 'Z':
        break
print(e - s + 1)
