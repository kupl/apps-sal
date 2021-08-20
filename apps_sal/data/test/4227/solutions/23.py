(N, M) = map(int, input().split())
G = [[] for _ in range(N)]
seen = [False] * N
for i in range(M):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)


def dfs(x, G, seen):
    seen[x] = True
    flag = True
    for i in seen:
        if i == False:
            flag = False
    if flag:
        return 1
    res = 0
    for i in G[x]:
        if seen[i]:
            continue
        res += dfs(i, G, seen)
        seen[i] = False
    return res


print(dfs(0, G, seen))
