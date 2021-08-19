count = []


def DFs(d, node, visited, c):
    visited.add(node)
    for i in d[node]:
        if i[0] not in visited:
            DFs(d, i[0], visited, c + i[1])
    count.append(c)


def dfs(d, n):
    visited = set()
    for i in d.keys():
        if i not in visited:
            c = 0
            DFs(d, i, visited, c)


n = int(input())
d = {}
for i in range(n):
    d[i] = []
for i in range(n - 1):
    (u, v, c) = map(int, input().split(' '))
    d[u].append([v, c])
    d[v].append([u, c])
dfs(d, n)
print(max(count))
