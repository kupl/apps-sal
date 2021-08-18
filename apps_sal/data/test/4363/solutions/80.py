import sys
import math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10**9)


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lint_dec(): return list(map(lambda x: int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]


K, S = lint()
ans = 0

for i in range(K + 1):
    for j in range(K + 1):
        if 0 <= S - i - j <= K:
            ans += 1

print(ans)
