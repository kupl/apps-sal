from collections import defaultdict
(N, M) = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(M):
    (x, y, z) = list(map(int, input().split()))
    x -= 1
    y -= 1
    edges[x].append(y)
    edges[y].append(x)
is_visited = [False] * N


def dfs(i):
    stack = [i]
    while stack:
        i = stack.pop()
        if is_visited[i]:
            continue
        is_visited[i] = True
        for j in edges[i]:
            stack.append(j)


islands = 0
for i in range(N):
    if is_visited[i] == False:
        islands += 1
        dfs(i)
print(islands)
