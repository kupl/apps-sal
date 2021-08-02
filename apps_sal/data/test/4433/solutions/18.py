from collections import deque as queue

n, m = list(map(int, input().split()))
used = [0] * n
edges = [[] for _ in range(n)]
a = []
q = queue(a, 200000)


def bfs(z):
    used[z] = 1
    q.append(z)
    while q:
        x = q.popleft()
        for i in edges[x]:
            if not used[i]:
                q.append(i)
                print(x + 1, i + 1)
                used[i] = 1


for i in range(m):
    a, b = list(map(int, input().split()))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

k = 0
for i in range(n):
    k = max(k, len(edges[i]))

for i in range(n):
    if len(edges[i]) == k:
        bfs(i)
        break
