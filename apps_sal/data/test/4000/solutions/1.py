import sys
from collections import deque
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    (v, to) = list(map(int, input().split()))
    v -= 1
    to -= 1
    g[v].append(to)
    g[to].append(v)
queue = deque([(0, 0)])
visited = [False] * n
while queue:
    (v, d) = queue.popleft()
    visited[v] = True
    for to in g[v]:
        if not visited[to]:
            queue.append((to, d + 1))
a = v
queue = deque([(a, 0)])
prev = [-1] * n
for i in range(n):
    visited[i] = False
while queue:
    (v, d) = queue.popleft()
    visited[v] = True
    for to in g[v]:
        if not visited[to]:
            queue.append((to, d + 1))
            prev[to] = v
(b, ctr) = (v, d)
for i in range(n):
    visited[i] = False
curr = prev[b]
nxt = b
prv = prev[curr]
add = 0
if a != 0 and b != 0:
    c = 0
elif a != 1 and b != 1:
    c = 1
else:
    c = 2
while curr != a:
    visited[curr] = True
    for to in g[curr]:
        if to == nxt or to == prv:
            continue
        queue = deque([(to, 1)])
        while queue:
            (v, d) = queue.popleft()
            visited[v] = True
            for to in g[v]:
                if not visited[to]:
                    queue.append((to, d + 1))
        if add < d:
            (c, add) = (v, d)
    nxt = curr
    curr = prev[curr]
    prv = prev[curr]
print(ctr + add)
print(a + 1, b + 1, c + 1)
