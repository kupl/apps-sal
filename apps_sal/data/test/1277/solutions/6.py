from collections import deque
from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, u, v = nii()
u -= 1
v -= 1

tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = nii()
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

dist_a = [-1 for i in range(n)]
dist_a[v] = 0

dist_t = [-1 for i in range(n)]
dist_t[u] = 0


def BFS(dist, s):
    que = deque()
    que.append(s)

    while que:
        x = que.popleft()
        for i in tree[x]:
            if dist[i] == -1:
                que.append(i)
                dist[i] = dist[x] + 1
    return dist


dist_a = BFS(dist_a, v)
dist_t = BFS(dist_t, u)

ans = 0
for i in range(n):
    if dist_a[i] > dist_t[i]:
        ans = max(ans, dist_a[i] - 1)

print(ans)
