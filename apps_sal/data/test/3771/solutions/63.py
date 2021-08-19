def dfs(v, t, f, used, graph):
    if v == t:
        return f
    used[v] = True
    for to in graph[v]:
        c = graph[v][to]
        if used[to] or c == 0:
            continue
        d = dfs(to, t, min(f, c), used, graph)
        if d > 0:
            graph[v][to] -= d
            graph[to][v] += d
            return d
    return 0


def max_flow(s, t, graph):
    flow = 0
    while True:
        used = [False] * len(graph)
        f = dfs(s, t, float('inf'), used, graph)
        flow += f
        if f == 0 or f == float('inf'):
            return flow


(H, W) = map(int, input().split())
a = [input() for _ in range(H)]
a = [[s for s in a[i]] for i in range(H)]
graph = [{} for _ in range(H + W + 2)]
for h in range(H):
    for w in range(W):
        if a[h][w] == 'o':
            graph[h][H + w] = 1
            graph[H + w][h] = 1
        if a[h][w] == 'S':
            graph[H + W][h] = float('inf')
            graph[H + W][H + w] = float('inf')
            graph[h][H + W] = 0
            graph[H + w][H + W] = 0
        if a[h][w] == 'T':
            graph[H + W + 1][h] = 0
            graph[H + W + 1][H + w] = 0
            graph[h][H + W + 1] = float('inf')
            graph[H + w][H + W + 1] = float('inf')
ans = max_flow(H + W, H + W + 1, graph)
if ans == float('inf'):
    ans = -1
print(ans)
