from collections import deque
N, M = map(int, input().split())

g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(u):
    queue = deque([u])
    ans = [None] * (N + 1)  # 距離が1小さい隣接点
    d = [None] * (N + 1)  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                ans[i] = v
                queue.append(i)
    return ans


# 0からの各頂点の距離
ans = bfs(1)
print('Yes')
for i in range(2, N + 1):
    print(ans[i])
