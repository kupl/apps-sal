import bisect
import math
import sys
sys.setrecursionlimit(10000000)


def input():
    return sys.stdin.readline()[:-1]


n, u, v = list(map(int, input().split()))
u -= 1
v -= 1
g = [[]for i in range(n)]
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
seen = [-1 for i in range(n)]
taka = []
aok = []


def dfs(s, lis):
    nec = g[s]
    if len(nec) == 1:
        lis.append(s)
    for i in nec:
        if seen[i] != -1:
            continue
        seen[i] = seen[s] + 1
        dfs(i, lis)


seen[u] = 0
dfs(u, taka)
takadist = [i for i in seen]
seen = [-1 for i in range(n)]
seen[v] = 0
dfs(v, aok)
ans = 0
for i in aok:
    if takadist[i] < seen[i]:
        ans = max(ans, seen[i])
if g[u] == [v]:
    print((0))
else:
    print((ans - 1))
