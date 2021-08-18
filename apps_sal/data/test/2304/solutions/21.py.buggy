# 解説みたよ
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n, m = list(map(int, input().split()))
es = [[] for i in range(n)]
l, r, d = [0] * m, [0] * m, [0] * m
for i in range(m):
    l[i], r[i], d[i] = list(map(int, input().split()))
    l[i] -= 1
    r[i] -= 1
    es[l[i]].append((r[i], d[i]))
    es[r[i]].append((l[i], -d[i]))
INF = 1000000000000
value = [INF] * n


def dfs(v):
    for i, di in es[v]:
        if value[i] == INF:
            value[i] = value[v] + di
            dfs(i)


for i in range(n):
    if value[i] == INF:
        value[i] = 0
        dfs(i)

for i, j, k in zip(l, r, d):
    if value[j] - value[i] != k:
        print("No")
        return
print("Yes")
