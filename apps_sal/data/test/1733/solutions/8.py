from collections import deque
import sys
input = sys.stdin.readline
(n, x, y) = list(map(int, input().split()))
x -= 1
y -= 1
graph = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = list(map(int, input().split()))
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
parent = [-1] * n
q = deque([x])
while q:
    node = q.popleft()
    if node == y:
        break
    for i in graph[node]:
        if i == parent[node]:
            continue
        parent[i] = node
        q.append(i)
node = y
y_ = parent[y]
while parent[node] != x:
    node = parent[node]
parent = [-1] * n
parent[x] = node
parent[y] = y_
(a, b) = (0, 0)
q = deque([x])
while q:
    node = q.popleft()
    a += 1
    for i in graph[node]:
        if i == parent[node]:
            continue
        parent[i] = node
        q.append(i)
q = deque([y])
while q:
    node = q.popleft()
    b += 1
    for i in graph[node]:
        if i == parent[node]:
            continue
        parent[i] = node
        q.append(i)
ans = n * (n - 1) - a * b
print(ans)
