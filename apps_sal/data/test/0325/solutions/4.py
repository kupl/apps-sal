from collections import deque


def dfs(edge, s):
    used = {s}
    que = deque([s])
    while que:
        v = que.pop()
        for u in edge[v]:
            if u in used:
                continue
            used.add(u)
            que.append(u)
    return used


def bellmanFord(edges):
    coins = [float('inf')] * N
    coins[0] = 0
    for _ in range(N):
        f = True
        for (u, v, c) in edges:
            if coins[u] + c < coins[v]:
                coins[v] = coins[u] + c
                f = False
        if f:
            return max(0, -coins[-1])
    return -1


(N, M, P) = map(int, input().split())
A = [[] for _ in range(N)]
A_rev = [[] for _ in range(N)]
E = [tuple()] * M
for i in range(M):
    (a, b, c) = map(int, input().split())
    a -= 1
    b -= 1
    c = P - c
    A[a].append(b)
    A_rev[b].append(a)
    E[i] = (a, b, c)
U = dfs(A, 0) & dfs(A_rev, N - 1)
F = [(a, b, c) for (a, b, c) in E if a in U and b in U]
print(bellmanFord(F))
