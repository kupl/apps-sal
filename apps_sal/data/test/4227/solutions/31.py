n, m = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

G = [list() for _ in range(n + 1)]
for a, b in edges:
    G[a].append(b)
    G[b].append(a)

checked = [False for _ in range(n)]

ans = 0

def dfs(v):
    nonlocal ans
    if all(checked):
        ans += 1
        return
    for u in G[v]:
        if not checked[u - 1]:
            checked[u - 1] = True
            dfs(u)
            checked[u - 1] = False
    return

checked[0] = True
dfs(1)
print(ans)

