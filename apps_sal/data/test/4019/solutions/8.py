n, m, D = [int(x) for x in input().split(' ')]

G = {}
for u in range(1, n + 1):
    G[u] = set()
for i in range(m):
    u, v = [int(x) for x in input().split(' ')]
    G[u].add(v)
    G[v].add(u)

if len(G[1]) < D:
    print('NO')
else:

    visited = [1] + [0] * n
    comp = [0] * (n + 1)
    c_visited = [1] + [0] * n

    a = 0
    for i in G[1]:
        if not visited[i]:
            a += 1
            comp[i] = a
            visited[i] = 1
            q = [i]
            while len(q) > 0:
                u = q.pop(0)
                for v in G[u]:
                    if v != 1 and not visited[v]:
                        q.append(v)
                        comp[v] = a
                        visited[v] = 1
    if a > D:
        print('NO')
    else:
        print('YES')
        d = D
        visited[1] = 2
        queue = []
        n_edges = 0
        for v in G[1]:
            if not c_visited[comp[v]]:
                visited[v] = 2
                d -= 1
                c_visited[comp[v]] = 1
                n_edges += 1
                print(1, v)
                queue.append(v)
        if d:
            for v in G[1]:
                if visited[v] != 2:
                    visited[v] = 2
                    d -= 1
                    print(1, v)
                    n_edges += 1
                    queue.append(v)
                    if not d:
                        break
        while len(queue) > 0 and n_edges < n - 1:
            u = queue.pop(0)
            for v in G[u]:
                if visited[v] != 2:
                    visited[v] = 2
                    queue.append(v)
                    n_edges += 1
                    print(u, v)
