from sys import stdin, setrecursionlimit


n = int(stdin.readline())
ay = [int(x) for x in stdin.readline().split()]

graph = [set() for x in range(n)]

for e in range(n - 1):
    a, b = [int(x) - 1 for x in stdin.readline().split()]
    graph[a].add(b)
    graph[b].add(a)

dists = {}
child = {}

bruh = sum(ay)
path = [(0, 0)]

for x, p in path:
    for y in graph[x]:
        if y != p:
            path.append((y, x))

for x, parent in path[::-1]:
    total = 0
    children = ay[x]
    for v in graph[x]:
        if v != parent:
            c, sm = child[v], dists[v]
            children += c
            total += sm + c
    dists[x] = total
    child[x] = children
b2, b3 = child[0], dists[0]

for x, parent in path:
    for v in graph[x]:
        if v != parent:
            dists[v] = dists[x] + bruh - child[v] * 2
print(max([dists[y] for y in range(n)]))
