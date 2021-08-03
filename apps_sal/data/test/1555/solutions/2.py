import sys

sys.setrecursionlimit(2000)


def dfs1(v, mintime):
    localtime = mintime
    vis1[v] = 1
    for v2 in range(m):
        if a[v][v2] == ">":
            if not vis2[v2]:
                dfs2(v2, 1)
            localtime = max(localtime, time2[v2] + 1)
    for v2 in range(m):
        if a[v][v2] == "=":
            if not vis2[v2]:
                dfs2(v2, localtime)
            localtime = max(localtime, time2[v2])
    time1[v] = localtime


def dfs2(v, mintime):
    localtime = mintime
    vis2[v] = 1
    for v2 in range(n):
        if a[v2][v] == "<":
            if not vis1[v2]:
                dfs1(v2, 1)
            localtime = max(localtime, time1[v2] + 1)
    for v2 in range(n):
        if a[v2][v] == "=":
            if not vis1[v2]:
                dfs1(v2, localtime)
            localtime = max(localtime, time1[v2])
    time2[v] = localtime


n, m = list(map(int, input().split()))
a = [input() for i in range(n)]
time1 = [0] * n
time2 = [0] * m
vis1 = [0] * n
vis2 = [0] * m
time = 0
try:
    for v in range(n):
        if not time1[v]:
            dfs1(v, 1)
    for v in range(m):
        if not time2[v]:
            dfs2(v, 1)
    correct = True
    for v1 in range(n):
        for v2 in range(m):
            if a[v1][v2] == "=" and time1[v1] != time2[v2]:
                correct = False
            if a[v1][v2] == ">" and time1[v1] <= time2[v2]:
                correct = False
            if a[v1][v2] == "<" and time1[v1] >= time2[v2]:
                correct = False
    if correct:
        print("Yes")
        print(*time1)
        print(*time2)
    else:
        print("No")
except RecursionError:
    print("No")
