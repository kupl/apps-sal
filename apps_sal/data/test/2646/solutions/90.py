from collections import deque
(n, m) = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
mark = [-1] * (n + 1)
mark[0] - 0
mark[1] = 0
d = deque()
d.append(1)
while d:
    v = d.popleft()
    for i in graph[v]:
        if mark[i] != -1:
            continue
        mark[i] = v
        d.append(i)
if '-1' in mark:
    print('No')
else:
    print('Yes')
    print(*mark[2:], sep='\n')
