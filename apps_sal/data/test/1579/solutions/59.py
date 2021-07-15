import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
edges = [[] for i in range(200000)]
for i in range(n):
    x, y = map(int, input().split())
    edges[x - 1].append(y + 99999)
    edges[y + 99999].append(x - 1)
ans = 0
visited = [0] * (200000)
cntx, cnty = 0, 0
def dfs(u):
    nonlocal cntx, cnty
    visited[u] = 1
    if u // 100000 >= 1:
        cnty += 1
    else:
        cntx += 1
    for i in edges[u]:
        if visited[i] == 0:
            dfs(i)
ans = -1 * n
for i in range(100000):
    if visited[i] == 0:
        cntx, cnty = 0, 0
        dfs(i)
        ans += cntx * cnty
print(ans)
