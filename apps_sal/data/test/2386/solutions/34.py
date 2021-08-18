import sys
import math
from itertools import combinations as c, permutations as perm, product as p
from collections import deque
sys.setrecursionlimit(10**9)
INF = float('inf')
MOD = 10**9 + 7


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lintdec(): return list(map(lambda x: int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]


N = ii()
A = lint()
B = [A[i] - i - 1 for i in range(N)]
B.sort()

if N % 2 == 1:
    m = B[N // 2]
    print(sum(abs(b - m) for b in B))
else:
    m = ((B[N // 2] + B[N // 2 - 1])) / 2
    print(int(sum(abs(b - m) for b in B)))
