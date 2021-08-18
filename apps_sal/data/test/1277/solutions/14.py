def resolve():
    N, u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    adjs = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = list([int(x) - 1 for x in input().split()])
        adjs[a].append(b)
        adjs[b].append(a)
    dist_from_u = [float("inf") for _ in range(N)]
    dist_from_u[u] = 0
    import collections
    q = collections.deque([u])
    while q:
        node = q.pop()
        for adj in adjs[node]:
            if dist_from_u[adj] > dist_from_u[node] + 1:
                dist_from_u[adj] = dist_from_u[node] + 1
                q.appendleft(adj)
    dist_from_v = [float("inf") for _ in range(N)]
    dist_from_v[v] = 0
    import collections
    q = collections.deque([v])
    while q:
        node = q.pop()
        for adj in adjs[node]:
            if dist_from_v[adj] > dist_from_v[node] + 1:
                dist_from_v[adj] = dist_from_v[node] + 1
                q.appendleft(adj)
    length = 0
    for i in range(N):
        if dist_from_u[i] < dist_from_v[i] and length < dist_from_v[i]:
            length = dist_from_v[i]
    print((length - 1))


def __starting_point():
    resolve()


__starting_point()
