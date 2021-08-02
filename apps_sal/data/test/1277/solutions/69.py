import sys
sys.setrecursionlimit(1 << 30)


def dfs(x, dis):
    for y in Tree[x]:
        if parent[y] != x:
            parent[x] = y
            dis[y] = dis[x] + 1
            dfs(y, dis)


N, u, v = map(int, input().split())
Tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    A, B = map(int, input().split())
    Tree[A].append(B)
    Tree[B].append(A)
disT = [-1] * (N + 1)
disA = [-1] * (N + 1)
disT[u] = 0
disA[v] = 0
parent = [-1] * (N + 1)
dfs(u, disT)
parent = [-1] * (N + 1)
dfs(v, disA)
Ans = 0
for i in range(len(disA)):
    if disA[i] >= disT[i]:
        Ans = max(Ans, disA[i] - 1)
print(Ans)
