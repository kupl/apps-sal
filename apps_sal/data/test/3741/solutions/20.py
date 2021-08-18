def solve(n, a):
    B = 60
    bits = [[] for i in range(B)]
    for i in range(n):
        for j in range(B):
            if a[i] & (1 << j):
                bits[j].append(i)

    adj = [[] for i in range(n)]
    for shared in bits:
        if len(shared) >= 3:
            return 3
        elif len(shared) == 2:
            u, v = shared
            adj[u].append(v)
            adj[v].append(u)

    vis = [False for u in range(n)]
    dist = [-1 for u in range(n)]

    def shortest_cycle(n, adj, s):
        frontier = [(s, -1)]
        dist[s] = 0
        ptr = 0

        while ptr < len(frontier):
            u, p = frontier[ptr]
            if not vis[u]:
                vis[u] = True
                for v in adj[u]:
                    if vis[v] and v != p:
                        ans = dist[u] + dist[v] + 1
                        for u, p in frontier:
                            vis[u] = False
                            dist[u] = -1
                        return ans
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        frontier.append((v, u))
            ptr += 1

        return 10**18

    ans = min([shortest_cycle(n, adj, i) for i in range(n)])
    if ans == 10**18:
        ans = -1

    return ans


print(solve(int(input()), list(map(int, input().split()))))
