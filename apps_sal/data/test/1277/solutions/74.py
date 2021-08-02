import sys
sys.setrecursionlimit(10**7)
N, T, A = list(map(int, input().split())); INF = float("inf")
T -= 1; A -= 1  # 0index
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a -= 1; b -= 1  # 0index
    G[a].append(b); G[b].append(a)

disT = [INF for _ in range(N)]; disT[T] = 0
disA = [INF for _ in range(N)]; disA[A] = 0


def dfs(v, L):
    for u in G[v]:
        if L[u] != INF:
            continue
        L[u] = L[v] + 1
        dfs(u, L)


dfs(T, disT)
dfs(A, disA)
# print(disT)
# print(disA)
ans = 0
for i in range(N):
    if disT[i] < disA[i]:
        ans = max(ans, disA[i] - 1)
print(ans)
