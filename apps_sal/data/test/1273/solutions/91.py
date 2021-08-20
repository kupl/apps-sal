from collections import deque


def main():
    n = int(input())
    adj = [[] for i in range(n + 1)]
    ab = [list(map(int, input().split())) for i in range(n - 1)]
    for (a, b) in ab:
        adj[a].append(b)
        adj[b].append(a)
    order = []
    parent = [0] * (n + 1)
    visited = [0] * (n + 1)
    visited[1] = 1
    q = deque([1])
    while q:
        par = q.popleft()
        order.append(par)
        for chl in adj[par]:
            if visited[chl]:
                continue
            visited[chl] = 1
            parent[chl] = par
            q.append(chl)
    cl = [None] * (n + 1)
    for par in order:
        pc = cl[par]
        color = 1
        for chl in adj[par]:
            if chl == parent[par]:
                continue
            if pc == color:
                color += 1
            cl[chl] = color
            color += 1
    g = max([len(i) for i in adj])
    print(g)
    for (a, b) in ab:
        if parent[a] != b:
            print(cl[b])
        else:
            print(cl[a])


def __starting_point():
    main()


__starting_point()
