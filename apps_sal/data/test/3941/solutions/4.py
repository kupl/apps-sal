import sys
(n, m) = map(int, input().split())
door = list(map(int, input().split()))
a = [[] for i in range(n + 1)]
e = [[] for i in range(m)]
color = [-1] * m
visited = [False] * m


def bfs(u, visited):
    color[u] = 0
    q = [u]
    h = 0
    visited[u] = True
    while h < len(q):
        u = q[h]
        h += 1
        for v in e[u]:
            if color[v[0]] == -1:
                color[v[0]] = color[u] ^ v[1]
                q.append(v[0])
                visited[v[0]] = True
            elif color[v[0]] != color[u] ^ v[1]:
                return False
    return True


for i in range(m):
    b = list(map(int, input().split()))
    for j in range(1, len(b)):
        k = b[j]
        a[k].append(i)
        if len(a[k]) == 2:
            e[a[k][0]].append((a[k][1], 1 - door[k - 1]))
            e[a[k][1]].append((a[k][0], 1 - door[k - 1]))
flag = True
for i in range(m):
    if color[i] == -1:
        if bfs(i, visited) == False:
            flag = False
            break
if flag:
    print('YES')
else:
    print('NO')
