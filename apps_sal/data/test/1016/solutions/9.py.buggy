#!/usr/env python3
path = []


def dfs(graph, node):
    nonlocal path
    path.append(node)
    for i in graph.get(node):
        if i not in path:
            dfs(graph, i)


n, m = list(map(int, input().split()))
a = {}
for i in range(m):
    x, y = list(map(int, input().split()))
    if x not in a:
        a.setdefault(x, [y])
    else:
        a[x].append(y)
    if y not in a:
        a.setdefault(y, [x])
    else:
        a[y].append(x)
for i in range(1, n + 1):
    if i not in a:
        a.setdefault(i, [])

dfs(a, 1)
totalpath = []
t = 0
for i in range(2, n + 1):
    #    print(i - 1, path, sorted(totalpath))
    if len(path) > 1:
        t += len(path) - 1
    totalpath += path
    path = []
    if i not in totalpath:
        dfs(a, i)

print(2 ** t)
