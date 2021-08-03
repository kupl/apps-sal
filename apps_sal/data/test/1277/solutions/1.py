import collections
def ma(): return list(map(int, input().split()))


n, u, v = ma()
u, v = u - 1, v - 1
tree = [[] for i in range(n)]

for i in range(n - 1):
    a, b = ma()
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
que = collections.deque([(v, 0)])
vis = [False] * n
dist_v = [0] * n
while que:
    now, c = que.popleft()
    vis[now] = True
    dist_v[now] = c
    for node in tree[now]:
        if not vis[node]:
            que.append((node, c + 1))
que = collections.deque([(u, 0)])
vis = [False] * n
dist_u = [0] * n
while que:
    now, c = que.popleft()
    vis[now] = True
    dist_u[now] = c
    for node in tree[now]:
        if not vis[node]:
            que.append((node, c + 1))
ans = 0
for i in range(n):
    if dist_u[i] < dist_v[i]:
        ans = max(ans, dist_v[i])
print((ans - 1))
