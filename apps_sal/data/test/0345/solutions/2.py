n, m = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
maxcnt = 0
for node1 in range(n):
    for node2 in range(node1 + 1, n):
        used = [[False] * n for _ in range(n)]
        col = list(range(0, node2)) + [node1] + list(range(node2 + 1, n))
        cnt = 0
        for u in range(n):
            for v in graph[u]:
                if not used[col[u]][col[v]]:
                    used[col[u]][col[v]] = used[col[v]][col[u]] = True
                    cnt += 1
        maxcnt = max(cnt, maxcnt)
print(maxcnt if n > 6 else m)
