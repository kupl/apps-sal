import sys, math
from itertools import combinations as c, product as p
from collections import deque
sys.setrecursionlimit(10**9)
INF = float('inf')
MOD = 10**9 + 7
#MOD = 998244353


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lintdec(): return list(map(lambda x:int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [int(input()) for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]



############################################################
N = ii()

ans = 0
S = []
for i in range(N):
    s = ii()
    ans += s
    S.append(s)

S.sort()
if ans % 10 == 0:
    for s in S:
        if s % 10:
            ans -= s
            break
    else:
        ans = 0

print(ans)
