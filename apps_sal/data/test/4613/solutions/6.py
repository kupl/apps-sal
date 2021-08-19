N, M = map(int, input().split())
G = [[] for _ in range(N)]
H = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1  # 0index
    G[a].append([b, i])
    G[b].append([a, i])  # iを辺のIDとして保存
    H.append([a, b])
ans = 0


def dfs(v, ID):  # IDの辺を使えない
    visited.add(v)
    for u, idx in G[v]:
        if idx == ID or u in visited:
            continue
        dfs(u, ID)


for i in range(M):
    visited = set([])
    start = H[i][0]
    goal = H[i][1]
    dfs(start, i)
    if goal not in visited:
        ans += 1
print(ans)
