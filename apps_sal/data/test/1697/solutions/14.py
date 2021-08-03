t, u = list(map(int, input().split(' ')))


def ok(x, y, inx):
    if not (0 <= x <= t - 1 and 0 <= y <= u - 1):
        return False
    if not inx[x][y]:
        return False
    return True


def dfs(graph, start, path=[]):
    inx = [[False] * u for _ in range(t)]
    for i in graph:
        a, b = i[0], i[1]
        inx[a][b] = True
    visited = [[False] * u for _ in range(t)]
    parent = [[0] * u for _ in range(t)]

    q = [start]

    while q:

        bd = q.pop(0)
        a = bd[0]
        b = bd[1]

        if not visited[a][b]:
            for bad in [(a - 1, b), (a, b - 1), (a + 1, b), (a, b + 1)]:
                x = bad[0]
                y = bad[1]
                if ok(x, y, inx):
                    if visited[x][y] and (x, y) != parent[a][b]:
                        return True
                    q = [(x, y)] + q
                    parent[x][y] = (a, b)
            visited[a][b] = True
    return False


graph = {}
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    graph[i] = []

for i in range(t):
    x = input()
    for j in range(u):
        graph[x[j]].append((i, j))

graph2 = {}
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if graph[i] != []:
        graph2[i] = graph[i]

for i in graph2:
    for e in graph2[i]:
        if dfs(graph2[i], e):
            print("Yes")
            quit()


print("No")
