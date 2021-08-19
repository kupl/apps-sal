from collections import deque
import sys
input = sys.stdin.readline
inf = pow(10, 10)
(n, m) = list(map(int, input().split()))
a = [inf] * n
edge = [[] for i in range(n)]
for i in range(m):
    (l, r, d) = list(map(int, input().split()))
    l -= 1
    r -= 1
    edge[l].append((r, d))
    edge[r].append((l, -d))
flag = True
dist = [inf] * n
for i in range(n):
    if not flag:
        break
    if dist[i] == inf:
        dist[i] = 0
        dq = deque([i])
        while dq:
            now = dq.popleft()
            for e in edge[now]:
                (nnode, d) = e
                if dist[nnode] == inf:
                    dist[nnode] = dist[now] + d
                    dq.append(nnode)
                elif dist[nnode] != dist[now] + d:
                    flag = False
                    break
if flag:
    print('Yes')
else:
    print('No')
