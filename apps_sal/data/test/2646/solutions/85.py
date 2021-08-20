from collections import deque
import sys
sys.setrecursionlimit(500 * 500)
(N, M) = map(int, input().split())
tree = [[] for _ in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]
for edge in edges:
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])
depth = [-1] * (N + 1)
depth[1] = 0
d = deque()
d.append(1)
ans = [0] * (N + 1)
while d:
    v = d.popleft()
    for i in tree[v]:
        if depth[i] != -1:
            continue
        depth[i] = depth[v] + 1
        ans[i] = v
        d.append(i)
print('Yes')
print(*ans[2:], sep='\n')
