def bfs(a, i, visited, connected):
    visited[i] = True
    q = list(a[i])
    j = 0
    while (j < len(q)):
        cur = q[j]
        if (not visited[cur]):
            connected.append(cur)
            visited[cur] = True
            for k in range(len(a[cur])):
                q.append(a[cur][k])
        j += 1

    return connected


def check(connected, a, n):
    if (len(connected) < 3):
        return False
    for i in range(1, len(connected)):
        node = connected[i]
        if (len(a[node]) != 2):
            return False
    return True


n, m = map(int, input().split())

a = []
visited = []

for i in range(n):
    a.append([])
    visited.append(False)

for i in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v - 1)
    a[v - 1].append(u - 1)

res = 0

for i in range(n):
    if (not visited[i]):
        connected = bfs(a, i, visited, [i])
        if (check(connected, a, n)):
            res += 1

print(res)
