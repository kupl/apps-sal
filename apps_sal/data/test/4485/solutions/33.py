(N, M) = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(goal, graph, seen, next_v):
    for x in graph[next_v[0][0]]:
        if x == goal:
            return True
        if x in seen:
            continue
        next_v.append((x, next_v[0][1] + 1))
        seen.add(x)
    return False


next_v = [(0, 0)]
seen = {0}
while True:
    if len(next_v) == 0 or next_v[0][1] == 2:
        ans = 'IMPOSSIBLE'
        break
    if bfs(N - 1, graph, seen, next_v):
        ans = 'POSSIBLE'
        break
    next_v.pop(0)
print(ans)
