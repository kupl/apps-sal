import copy
from collections import deque
(n, m) = map(int, input().split())
e = [[] for i in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
visited = [False] * n
visited[0] = True
d = deque([[0, visited]])
cnt = 0
while d:
    (f, visited) = d.pop()
    for t in e[f]:
        v = copy.deepcopy(visited)
        if not v[t]:
            v[t] = True
            if False in v:
                d.append([t, v])
            else:
                cnt += 1
print(cnt)
