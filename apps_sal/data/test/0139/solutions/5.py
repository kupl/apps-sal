have = False
cycle_begin, block_u, block_v = -1, -1, -1
g, mark, cycle = [], [], []


def dfs(u):
    nonlocal have, cycle_begin
    mark[u] = 1
    for v in g[u]:
        if u == block_u and v == block_v:
            continue
        if mark[v] == 0:
            if dfs(v):
                if have:
                    cycle.append(u)
                if u == cycle_begin:
                    have = False
                return True
        elif mark[v] == 1:
            have = True
            cycle_begin = v
            cycle.append(u)
            return True
    mark[u] = 2
    return False


n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]
mark = [0 for _ in range(n)]

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
    cycle.append(cycle[0])
    for u in range(len(cycle) - 1, 0, -1):
        block_u = cycle[u]
        block_v = cycle[u - 1]
        mark = [0 for _ in range(n)]
        ok = True
        for u in range(n):
            if mark[u] == 0 and dfs(u):
                ok = False
                break
        if ok:
            print("YES")
            return

    print("NO")

