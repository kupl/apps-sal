def main():
    import sys
    input = sys.stdin.readline

    def find(a):
        upd = []
        cur = a
        while par[cur] != cur:
            upd.append(cur)
            cur = par[cur]
        for x in upd:
            par[x] = cur
        return cur

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if height[b] > height[a]:
            a, b = b, a
        par[b] = a
        if height[a] == height[b]:
            height[a] += 1

    def mst():
        ret = []
        for edge in edges:
            u, v, w = edge
            u = find(u)
            v = find(v)
            if u != v:
                union(u, v)
                ret.append(edge)
        return ret

    def dfs(u, par):
        for v, w in adj[u]:
            if v != par:
                dist[v] = max(dist[u], w)
                dfs(v, u)

    def bfs(u):
        visit = [False] * (n + 1)
        from collections import deque

        dq = deque()
        dq.append(u)
        visit[u] = True
        while dq:
            u = dq.popleft()
            for v, w in adj[u]:
                if not visit[v]:
                    dist[v] = max(dist[u], w)
                    dq.append(v)
                    visit[v] = True

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    par = [0] * (n + 1)
    height = [1] * (n + 1)
    for i in range(1, n + 1):
        par[i] = i
        height[i] = 1
    edges = []
    for i in range(m):
        edge = tuple(map(int, input().split()))
        edges.append(edge)
    edges.sort(key=lambda x: x[2])
    edges = mst()
    adj = [list() for i in range(n + 1)]
    for edge in edges:
        u, v, w = edge
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [0] * (n + 1)
    bfs(a[0])
    ans = 0
    for x in a:
        ans = max(ans, dist[x])
    ans = [ans] * k
    print(*ans)


main()
