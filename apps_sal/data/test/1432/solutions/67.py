import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ni()
A = na()
tmp = 0
now = 1
for i in range(N):
    A[i] *= 2
    tmp += now  * A[i]
    now *= -1

ans = [0] * N
ans[0] = tmp // 2
for i in range(N-1):
    ans[i+1] = A[i] - ans[i]
ans[N-1] = A[N-1] - ans[0]
print(*ans)
