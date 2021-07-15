import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

ans = [0] * 101010

S = ns()
dp=[[0 for i in range(101010)] for j in range(34)]

N = len(S)
for i in range(N):
    dp[0][i] = (i - 1) if S[i] == 'L' else (i + 1)

for p in range(33):
    for i in range(N):
        dp[p+1][i] = dp[p][dp[p][i]]

for i in range(N):
    ans[dp[32][i]] += 1

print(*ans[:N])
