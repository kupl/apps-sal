from collections import defaultdict


def colour(a, graph, cur, i):
    top = set()
    top.add(i)
    while len(top):
        x = top.pop()
        a[x] = cur
        for y in graph[x]:
            if a[y] == 0:
                top.add(y)


def colour_graph(a, graph, n):
    cur = 0
    for i in range(1, n + 1):
        if a[i] or i not in graph:
            continue
        else:
            cur += 1
            colour(a, graph, cur, i)


def count(col):
    ans = 0
    for el in col:
        if col[el] > 1:
            ans += col[el] * (col[el] - 1)
    return ans


n = int(input())
graph0 = defaultdict(set)
graph1 = defaultdict(set)
vertex0 = set()
a0 = [0] * (n + 1)
a1 = [0] * (n + 1)
for i in range(n - 1):
    (x, y, c) = list(map(int, input().split()))
    if c == 0:
        graph0[x].add(y)
        graph0[y].add(x)
        vertex0.add(x)
        vertex0.add(y)
    else:
        graph1[x].add(y)
        graph1[y].add(x)
colour_graph(a0, graph0, n)
colour_graph(a1, graph1, n)
answer = 0
col0 = defaultdict(int)
col1 = defaultdict(int)
for i in range(n + 1):
    if a0[i]:
        col0[a0[i]] += 1
    if a1[i]:
        col1[a1[i]] += 1
answer += count(col0) + count(col1)
col = defaultdict(int)
for v in vertex0:
    col[a1[v]] += col0[a0[v]] - 1
for el in col:
    if el:
        answer += col[el] * (col1[el] - 1)
print(answer)
