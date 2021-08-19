import sys
sys.setrecursionlimit(10 ** 9)
(N, Q) = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    G[b].append(a)
    G[a].append(b)
ans = [0] * N
for _ in range(Q):
    (p, x) = map(int, input().split())
    p -= 1
    ans[p] += x


def dfs(v, p):
    for to in G[v]:
        if to == p:
            continue
        ans[to] += ans[v]
        dfs(to, v)


dfs(0, -1)
for i in range(N):
    print(ans[i], end=' ')
