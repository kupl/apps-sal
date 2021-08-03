from collections import deque
def nii(): return map(int, input().split())


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


def BFS(s):
    dist = [-1 for i in range(n)]
    dist[s] = 0

    que = deque()
    que.append(s)

    while que:
        x = que.popleft()
        for i in tree[x]:
            if dist[i] == -1:
                que.append(i)
                dist[i] = dist[x] + 1
    return dist


dist_t = BFS(u)
dist_a = BFS(v)

ans = 0
for i in range(n):
    if dist_a[i] > dist_t[i]:
        ans = max(ans, dist_a[i] - 1)

print(ans)
