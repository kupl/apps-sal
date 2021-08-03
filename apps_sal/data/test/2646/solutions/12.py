from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)
dist = [-1] * n
d = deque()
d.append(0)
now = 0
while d:
    x = d.popleft()
    for i in range(len(edge[x])):
        if dist[edge[x][i]] == -1:
            dist[edge[x][i]] = x + 1
            d.append(edge[x][i])
print("Yes")
for i in range(n - 1):
    print(dist[i + 1])
