from collections import defaultdict as dd
g = dd(list)


def addE(u, v):
    g[u].append(v)
    g[v].append(u)


def dfs(v):
    stck = []
    stck.append(v)
    cost1 = cost[v - 1]
    visited[v] = True
    while len(stck) != 0:
        cur = stck.pop()
        for ch in g[cur]:
            if visited[ch]:
                continue
            cost1 = min(cost1, cost[ch - 1])
            stck.append(ch)
            visited[ch] = True
    return cost1


n, m = list(map(int, input().split()))
cost = [int(x) for x in input().split()]
visited = [False] * (n + 1)
for i in range(m):
    u, v = list(map(int, input().split()))
    addE(u, v)
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        ans += dfs(i)


for i in range(1, n + 1):
    if not visited[i]:
        ans += cost[i - 1]
print(ans)
