N, U, V = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    edge[x].append(y)
    edge[y].append(x)


def dist(s):
    dist = [-1] * (N + 1)
    node = [s]
    dist[s] = 0
    while node:
        s = node.pop()
        for t in edge[s]:
            if dist[t] == -1:
                dist[t] = dist[s] + 1
                node.append(t)
    return dist


taka = dist(U)
aoki = dist(V)
can_go = taka[V]

ans = 0
for t, a in zip(taka[1:], aoki[1:]):
    if t <= a:
        ans = max(ans, a - 1)
print(ans)
