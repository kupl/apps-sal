from collections import deque
N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = [int(x) for x in input().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
branch_list = [0 for i in range(N)]


def bfs(u):
    queue = deque([u])
    d = [None] * N
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
                branch_list[i] = v + 1
    return d


d = bfs(0)
for i in range(1, len(branch_list)):
    if branch_list[i] == 0:
        print("No")
        break
    if i == 1:
        print("Yes")
    print(branch_list[i])
