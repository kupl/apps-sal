import sys

n, m = [int(x) for x in input().split()]
E = [[] for i in range(1, n+1)]
for line in sys.stdin:
    u, v = [int(x) - 1 for x in line.split()]
    E[u].append(v)
    E[v].append(u)

ans = 0
visited = [False] * n
for v in range(n):
    if visited[v]:
        continue
    hasCycle = False
    stack = [(v, v)]
    while stack:
        node, p = stack.pop()
        if visited[node]:
            hasCycle = True
        else:
            visited[node] = True
            for u in E[node]:
                if u != p:
                    stack.append((u, node))
    ans += 0 if hasCycle else 1

print(ans)

