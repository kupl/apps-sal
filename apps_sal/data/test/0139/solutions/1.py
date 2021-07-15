n, m = [int(x) for x in input().split()]
a = [[] for i in range(n)]
for i in range(m):
    u, v = [int(x) for x in input().split()]
    a[u - 1].append(v - 1)

color = [0] * n # 0 - white, 1 - grey, 2 - black
cycle = []
blocked_u, blocked_v = -1, -1

def dfs(u):
    nonlocal color
    nonlocal cycle
    if color[u]:
        return
    color[u] = 1
    for v in a[u]:
        if u == blocked_u and v == blocked_v:
            continue
        if color[v] == 0:
            dfs(v)
        if color[v] == 1 or cycle:
            if not(cycle):
                cycle.append(v)
            cycle.append(u)
            return True
    color[u] = 2
    return False

def find_cycle():
    nonlocal color
    nonlocal cycle
    color = [0] * n # 0 - white, 1 - grey, 2 - black
    cycle = []
    for u in range(n):
        if dfs(u):
            break
    result = cycle[::-1]
    return {(result[i], result[(i + 1) % len(result)]) for i in range(len(result))}

cur = find_cycle()
if not(cur):
    print('YES')
    return

for bu, bv in cur:
    blocked_u = bu
    blocked_v = bv
    new = find_cycle()

    if not(new):
        print('YES')
        return

print('NO')

