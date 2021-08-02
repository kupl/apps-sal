from collections import deque
n, m = map(int, input().split())
u = []
v = []
g = [[] for _ in range(n)]

for i in range(m):
    uu, vv = map(int, input().split())
    u.append(uu)
    v.append(vv)
    g[uu - 1].append(vv - 1)

s, t = map(int, input().split())
s -= 1
t -= 1


def bfs(u):
    queue1 = deque([u])
    queue2 = deque([0])
    d = []
    for i in range(n):
        d.append([-1] * 3)
    d[u][0] = 0
    while queue1:
        v = queue1.popleft()
        l = queue2.popleft()
        nl = (l + 1) % 3
        for i in g[v]:
            if d[i][nl] is -1:
                d[i][nl] = d[v][l] + 1
                queue1.append(i)
                queue2.append(nl)
    return d


d = bfs(s)

ans = int(d[t][0] / 3)
if d[t][0] == -1:
    ans = -1
print(ans)
