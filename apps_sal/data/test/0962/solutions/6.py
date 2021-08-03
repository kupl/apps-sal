from collections import deque

n, m = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]
INF = 10 ** 5

adj = [[] for _ in range(n)]
for a, b in ab:
    a -= 1
    b -= 1
    adj[a].append(b)

mn = INF
for s in range(n):
    dq = deque([s])
    d = [-1] * n
    p = [-1] * n
    d[s] = 0
    last = []

    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                p[v] = u
                dq.append(v)

            if v == s:
                last.append(u)

    for v in last:
        route = [v]
        while p[v] != s:
            v = p[v]
            route.append(v)

        route.append(s)
        size = len(route)
        if size < mn:
            mn = size
            ans = route[::-1]

if mn != INF:
    print(mn)
    for e in ans:
        print((e + 1))
else:
    print((-1))
