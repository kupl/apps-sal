cycle_begin, block_u, block_v = -1, -1, -1
g, mark, prev, cycle = [], [], [], []


def dfs(u):
    nonlocal cycle_begin
    mark[u] = 1
    for v in g[u]:
        if u == block_u and v == block_v:
            continue
        if mark[v] == 0:
            prev[v] = u
            if dfs(v):
                return True
        elif mark[v] == 1:
            prev[v] = u
            cycle_begin = u
            return True
    mark[u] = 2
    return False


n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]
mark = [0 for _ in range(n)]
prev = [0 for _ in range(n)]

for _ in range(m):
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
    u = cycle_begin
    while u != cycle_begin or len(cycle) == 0:
        cycle.append(u)
        u = prev[u]
    cycle.append(cycle_begin)
    
    for u in range(len(cycle) - 1, 0, -1):
        block_u = cycle[u]
        block_v = cycle[u - 1]
        mark = [0 for _ in range(n)]
        have = False
        for u in range(n):
            if mark[u] == 0 and dfs(u):
                have = True
                break
        if not have:
            print("YES")
            return

    print("NO")

