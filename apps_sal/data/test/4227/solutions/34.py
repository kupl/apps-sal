N, M = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
cnt = [0]


def dfs(V, s):
    V[s] = 1
    if sum(V) == N:
        cnt[0] += 1
    else:
        for adj in G[s]:
            if V[adj] == 0:
                dfs(V[:adj] + [1] + V[adj + 1:], adj)


dfs([0] * N, 0)
print((cnt[0]))
