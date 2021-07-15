from collections import deque

n, m = map(int, input().split())
e = []
a = [[] for i in range(n)]

for i in range(m):
    fr, to = map(int, input().split())
    e.append((fr, to))
    a[fr - 1].append(to - 1)
    a[to - 1].append(fr - 1)

root = 0
maxPow = 0
for i in range(n):
    if len(a[i]) > maxPow:
        root = i
        maxPow = len(a[i])

visited = set()
d = deque()

d.append(root)
visited.add(root)
while len(d) != 0:
    cur = d.popleft()
    for adj in a[cur]:
        if adj not in visited:
            print(cur + 1, adj + 1)
            visited.add(adj)
            d.append(adj)
