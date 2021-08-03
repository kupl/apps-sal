N, M = map(int, input().split())
G = {}
for i in range(M):
    a, b = map(int, input().split())
    if a not in G:
        G[a] = set()
    if b not in G:
        G[b] = set()
    G[a].add(b)
    G[b].add(a)


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for i in graph[node]:
                stack.append(i)
    return visited


arr = []
seen = set()
for x in G:
    if x not in seen:
        P = dfs(G, x)
        seen |= P
        arr.append((list(P)[0], P))
cnt = 0
for x in arr:
    if x[0] in x[1] and all([len(G[y]) == 2 for y in x[1]]):
        cnt += 1
print(cnt)
