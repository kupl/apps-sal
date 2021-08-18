import sys
sys.setrecursionlimit(10000000)

V = 100005
N = int(input())

lines = [[] for _ in range(V * 2)]
visited = [False] * V * 2

count = []


def dfs(v):
    nonlocal count
    if visited[v]:
        return
    visited[v] = True
    count[v // V] += 1
    for u in lines[v]:
        dfs(u)


for i in range(N):
    x, y = [int(x) for x in input().split()]
    y += V
    lines[x].append(y)
    lines[y].append(x)

ans = 0
for i in range(V * 2):
    if visited[i]:
        continue
    count = [0, 0]
    dfs(i)
    ans += count[0] * count[1]

ans -= N
print(ans)
