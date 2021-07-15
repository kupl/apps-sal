import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n = ni()
ab = [na() for _ in range(n)]
ab.sort(key=itemgetter(1, 0))
now = 0
ans = 'Yes'
for i in range(n):
    a, b = ab[i]
    now += a
    if now > b:
        ans = 'No'
        break
print(ans)
