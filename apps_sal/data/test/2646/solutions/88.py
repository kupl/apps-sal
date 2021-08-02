from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

yet = [-1 for _ in range(n + 1)]
yet[0] = 0
yet[1] = 1

d = deque([1])

while d:
    v = d.popleft()
    for i in g[v]:
        if yet[i] == -1:
            yet[i] = v
            d.append(i)

ans = yet[2:]
print("Yes")
print(*ans, sep="\n")
