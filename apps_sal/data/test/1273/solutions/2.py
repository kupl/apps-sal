N = int(input())
graph = [[] for _ in range(N + 1)]
AB = []

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
    AB.append((a, b))

root = 1
parent = [0] * (N + 1)
order = []
stack = [root]

while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)

color = [-1] * (N + 1)
K = -1
for x in order:
    ng = color[x]
    c = 1
    for y in graph[x]:
        if y == parent[x]:
            continue
        if c == ng:
            c += 1
        K = max(c, K)
        color[y] = c
        c += 1

ans = []

for a, b in AB:
    if parent[a] == b:
        ans.append(color[a])
    else:
        ans.append(color[b])

print(K)
for i in ans:
    print(i)
