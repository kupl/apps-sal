import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

H, W = na()
N = ni()
a = na()
ans = []
for i in range(N):
    for _ in range(a[i]):
        ans.append(i+1)
for i in range(H):
    if i % 2 == 0:
        print(*ans[i*W:(i+1)*W])
    else:
        print(*ans[i*W:(i+1)*W][::-1])
