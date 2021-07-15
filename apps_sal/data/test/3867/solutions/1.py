from collections import deque
n = int(input())
graph = [set() for i in range(n + 1)]
graph[0].add(1)
graph[1].add(0)
for i in range(n - 1):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)
a = list(map(int, input().split()))
q = deque()
q.append(0)
i = 0
par = [0] * (n + 1)
while len(q):
    v = q.popleft()
    graph[v].discard(par[v])
    l = len(graph[v])
    if graph[v] != set(a[i:i + l]):
        print("No")
        break
    for j in range(i, i + l):
        q.append(a[j])
        par[a[j]] = v
    i += l
else:
    print("Yes")
