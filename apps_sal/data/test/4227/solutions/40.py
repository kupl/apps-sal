N, M = map(int, input().split())
Edge = [tuple(map(int, input().split())) for _ in range(M)]

Graph = [[] for _ in range(N)]
for a, b in Edge:
    Graph[a - 1].append(b - 1)
    Graph[b - 1].append(a - 1)

seen = set()


def dfs(v):
    seen.add(v)
    if len(seen) == N:
        seen.remove(v)
        return 1
    Res = [dfs(nv) for nv in Graph[v] if not nv in seen]
    seen.remove(v)
    return sum(Res)


print(dfs(0))
