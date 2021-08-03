import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int, read().split())
AB = list(zip(m, m))

graph = [[] for _ in range(N + 1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

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
for x in order:
    ng = color[x]
    c = 1
    for y in graph[x]:
        if y == parent[x]:
            continue
        if c == ng:
            c += 1
        color[y] = c
        c += 1

answer = []
for a, b in AB:
    if parent[a] == b:
        answer.append(color[a])
    else:
        answer.append(color[b])
K = max(answer)

print(K)
print('\n'.join(map(str, answer)))
