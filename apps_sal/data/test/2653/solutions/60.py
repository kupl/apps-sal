#!/usr/bin/env python3
from sys import setrecursionlimit

setrecursionlimit(10 ** 8)


def dfs(now):
    seen[now] = True
    score[now] += operation[now]
    for next in branch[now]:
        if seen[next] is False:
            score[next] += score[now]
            dfs(next)


N, Q = map(int, input().split())
branch = [set() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    branch[a - 1].add(b - 1)
    branch[b - 1].add(a - 1)
operation = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    operation[p - 1] += x

seen = [False] * N
score = [0] * N
for i in range(N):
    if seen[i] is False:
        dfs(i)

for ans in score:
    print(ans, end=' ')
