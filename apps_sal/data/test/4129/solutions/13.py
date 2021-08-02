from collections import deque
import sys
sys.setrecursionlimit(1000000)


n, m, s = [int(x) for x in input().split()]
adj = [[] for u in range(n + 1)]
vis = [False for u in range(n + 1)]
for i in range(m):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)


def tarjan():
    low = [-1 for u in range(n + 1)]
    disc = [-1 for v in range(n + 1)]
    in_stack = [False for v in range(n + 1)]
    st = deque()
    comp = []

    def dfs(u):
        dfs.dfs_time = dfs.dfs_time + 1
        low[u] = dfs.dfs_time
        disc[u] = dfs.dfs_time
        in_stack[u] = True
        st.append(u)

        for v in adj[u]:
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], disc[v])

        if low[u] == disc[u]:
            comp.append([])
            while u != st[-1]:
                x = st.pop()
                in_stack[x] = False
                comp[-1].append(x)
            x = st.pop()
            in_stack[x] = False
            comp[-1].append(x)

    dfs.dfs_time = 0
    for i in range(1, n + 1):
        if disc[i] == -1:
            dfs(i)

    return comp[::-1]


def visit(adj, vis, src):
    q = deque()
    q.append(src)
    vis[src] = True
    while len(q) > 0:
        u = q.popleft()
        for v in adj[u]:
            if vis[v] == False:
                vis[v] = True
                q.append(v)


ans = 0
visit(adj, vis, s)
tarOrd = tarjan()
for lis in tarOrd:
    x = lis[0]
    if vis[lis[0]] == False:
        visit(adj, vis, x)
        ans += 1

print(ans)
