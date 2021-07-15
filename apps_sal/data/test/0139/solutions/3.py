cycle_begin, cycle_end = -1, -1
g, mark, prev, edges = [], [], [], []

def dfs(u):
    nonlocal cycle_begin, cycle_end
    mark[u] = 1
    for v in g[u]:
        if mark[v] == 0:
            prev[v] = u
            if dfs(v):
                return True
        elif mark[v] == 1:
            cycle_begin = v
            cycle_end = u
            return True
    mark[u] = 2
    return False

def dfs2(u):
    mark[u] = 1
    for v in g[u]:
        if v != -1:
            if mark[v] == 0:
                if dfs2(v):
                    return True
            elif mark[v] == 1:
                return True
    mark[u] = 2
    return False

n, m = list(map(int, input().split()))
g = [[] for i in range(n)]
mark = [0 for i in range(n)]
prev = [-1 for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    u -= 1
    v -= 1
    g[u].append(v)
for i in range(n):
    if mark[i] == 0 and dfs(i):
        break
if cycle_begin == -1:
    print("YES")
else:
    cycle = []
    i = cycle_end
    while i != cycle_begin:
        cycle.append(i)
        i = prev[i]
    cycle.append(cycle_begin)
    cycle.reverse()
    edges = []
    for i in range(len(cycle) - 1):
        edges.append(tuple((cycle[i], cycle[i + 1])))
    edges.append(tuple((cycle[len(cycle) - 1], cycle[0])))
    can = False
    while len(edges) > 0:
        f = edges[0][0]
        s = edges[0][1]
        g[f][g[f].index(s)] = -1
        mark = [0 for i in range(n)]
        have = False
        for i in range(n):
            if mark[i] == 0 and dfs2(i):
                have = True
                break
        g[f][g[f].index(-1)] = s
        if not have:
            can = True
            break
        edges.pop(0)
    if can:
        print("YES")   
    else:
        print("NO")

