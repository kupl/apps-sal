import sys
sys.setrecursionlimit(10**6)

MAXVAL = 10**5
N = int(input())
edge = [[] for _ in range(MAXVAL * 2)]
visited = [0] * (MAXVAL * 2)
ans = 0
xnum = 0
ynum = 0
nodes = 0


def dfs(n):
    nonlocal xnum, ynum, nodes
    if visited[n] == 1:
        return True
    if n < MAXVAL:
        xnum += 1
    else:
        ynum += 1
    visited[n] = 1
    for item in edge[n]:
        nodes += 1
        dfs(item)
    return True


for i in range(N):
    x, y = [int(item) for item in input().split()]
    x -= 1
    y -= 1
    edge[x].append(y + MAXVAL)
    edge[y + MAXVAL].append(x)

for i in range(MAXVAL * 2):
    if visited[i] == 1:
        continue
    xnum = 0
    ynum = 0
    nodes = 0
    dfs(i)
    if nodes >= 3:
        ans += xnum * ynum - nodes // 2
print(ans)
