N, M = list(map(int, input().split()))

edge = []
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    edge.append((a, b))
    graph[a].append(b); graph[b].append(a)

def dfs(now):
    searched[now] = True
    for next in graph[now]:
        if searched[next]:
            continue
        if min(now, next) == a and max(now, next) == b:
            continue
        dfs(next)

ans = M
for i in range(M):
    a, b = edge[i]
    searched = [False] * N
    dfs(0)
    if sum(searched) == N:
        ans -= 1

print(ans)

