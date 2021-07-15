n = int(input())
ab = []
for i in range(n-1):
    a, b = map(int,input().split())
    ab.append([a, b])

graph = [[] for _ in range(n+1)]
for a,b in ab:
    graph[a].append(b)
    graph[b].append(a)

root = 1
parent = [0] * (n+1)
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
        
color = [-1] * (n+1)
for x in order:
    ng = color[x]
    c = 1
    for y in graph[x]:
        if y == parent[x]:
            continue # 子に対応させる
        if c == ng:
            c += 1
        color[y] = c
        c += 1

print(max(color))
for a,b in ab:
    if parent[a] == b:
        print(color[a])
    else:
        print(color[b])
