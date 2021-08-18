import sys
import math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10**9)


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lint(): return list(map(int, input().split()))
def lint_dec(): return list(map(lambda x: int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]


W, H, N = lint()
queue = lint_list(N)

xmin = max([x for x, y, a in queue if a == 1] + [0])
xmax = min([x for x, y, a in queue if a == 2] + [W])
ymin = max([y for x, y, a in queue if a == 3] + [0])
ymax = min([y for x, y, a in queue if a == 4] + [H])

print(max(0, xmax - xmin) * max(0, ymax - ymin))
