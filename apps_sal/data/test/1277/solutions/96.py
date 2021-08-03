from collections import deque
N, u, v = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    g[A - 1].append(B - 1)
    g[B - 1].append(A - 1)


def bfs(n):
    stack = deque([])
    depth = [-1] * N
    depth[n - 1] = 0
    stack.append(n - 1)
    while stack:
        a = stack.popleft()
        for b in g[a]:
            if depth[b] == -1:
                depth[b] = depth[a] + 1
                stack.append(b)
    return depth


U = bfs(u)
V = bfs(v)
List = []
for i in range(N):
    if len(g[i]) == 1 and U[i] < V[i]:
        List.append(i)
ans = 0

for i in List:
    ans = max(ans, V[i] - 1)

print(ans)
