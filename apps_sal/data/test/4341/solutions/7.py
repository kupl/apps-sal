import sys
input = sys.stdin.readline
(N, M) = map(int, input().split())
G = {}
for _ in range(M):
    (a, b) = map(int, input().split())
    if a not in G:
        G[a] = set()
    if b not in G:
        G[b] = set()
    G[a].add(b)
    G[b].add(a)
seen = set()


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for next in graph[node] - set(path):
            if next == goal:
                yield (path + [next])
            else:
                stack.append((next, path + [next]))


CC = []
for x in G:
    if x not in seen:
        P = dfs(G, x)
        seen |= P
        CC.append((list(P)[0], P))
cnt = 0
for x in CC:
    if x[0] in x[1] and all([len(G[y]) == 2 for y in x[1]]):
        cnt += 1
print(cnt)
