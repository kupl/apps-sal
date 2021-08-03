n, m = list(map(int, input().split()))
adj = [[0] * (n + 1) for _ in range(n + 1)]  # idx; 1~n
edges = [tuple(map(int, input().split())) for _ in range(m)]
cnt = 0

for e in edges:
    x, y = e
    adj[x][y] = 1
    adj[y][x] = 1


def dfs(s):
    seen[s] = 1
    for nx in range(1, n + 1):
        if adj[s][nx]:
            if seen[nx]:
                continue
            dfs(nx)


for bridge in edges:
    bx, by = bridge
    adj[bx][by] = 0  # 道を除く
    adj[by][bx] = 0
    seen = [0] * (n + 1)
    dfs(1)  # 1から深さ優先探索seenを埋める
    is_ok = 1
    if any(seen[i] == 0 for i in range(1, n + 1)):
        is_ok = 0
    if not is_ok:
        cnt += 1
    adj[bx][by] = 1  # 道を戻す
    adj[by][bx] = 1

print(cnt)
