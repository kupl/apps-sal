def rd(): return list(map(int, input().split()))


n, m, s, t = rd()
a = [0] * (n + 1)
b = a + []
G = [[] for i in range(n + 1)]
for i in range(m):
    u, v = rd()
    G[u].append(v)
    G[v].append(u)


def bfs(x, a):
    q = [x]
    while q:
        c = q.pop()
        for y in G[c]:
            if not a[y]:
                a[y] = a[c] + 1
                q.insert(0, y)
    a[x] = 0


bfs(s, a)
bfs(t, b)
print(sum(min(a[i] + b[j], a[j] + b[i]) > a[t] - 2 for i in range(1, n + 1) for j in range(i + 1, n + 1)) - m)
