import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

A, B, X = na()
ans = 0
for dn in range(18 + 1):
    s = X - dn * B
    tmp = s // A
    N = min(tmp, 10**9)
    if len(str(N)) == dn:
        ans = max(ans, N)
    else:
        t = 10 ** dn - 1
        if N >= t:
            ans = max(ans, t)
print(min(ans, 10 ** 9))
