import copy
from collections import deque
N, M = map(int, input().split())
lsside = [[] for i in range(N + 1)]
lsline = []
for i in range(M):
    a, b = map(int, input().split())
    lsside[a].append(b)
    lsside[b].append(a)
    lsline.append([a, b])

ans = 0
lsloop = []
for i in range(M):
    graph = copy.deepcopy(lsside)
    a = lsline[i][0]
    b = lsline[i][1]
    graph[a].remove(b)
    graph[b].remove(a)
    used = [False for i in range(N + 1)]
    ii = 1
    d = deque()
    d.append(a)
    used[a] = True
    while d:
        v = d.popleft()
        for i in graph[v]:
            if used[i]:
                continue
            ii += 1
            d.append(i)
            used[i] = True
    lsloop.append(ii)
ans = M - lsloop.count(N)
print(ans)
