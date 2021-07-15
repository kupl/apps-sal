n, m = list(map(int, input().split()))
edges = [[] for _ in range(n)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    edges[a-1].append(b-1)


def get_first_cycle(n, edges):
    seen = [-1] * n  # seen: -1: 未確認, 0: 非cycleのnode, 1: cycle候補
    for start in range(n):
        if seen[start] == 0:
            continue
        seen[start] = 1
        path = [start]
        while path:
            now = path[-1]
            if not edges[now]:
                path.pop()
                seen[now] = 0
                continue

            next_node = edges[now].pop()
            if seen[next_node] == -1:
                path.append(next_node)
                seen[next_node] = 1

            elif seen[next_node] == 1:
                idx = path.index(next_node)
                cycle = path[idx:]
                return cycle
    return False


cycle = get_first_cycle(n, edges)
if not cycle:
    print((-1))
    return

nodes = set(cycle)
length = len(cycle)
i = 0
while i < length:
    now = cycle[i]
    routes = edges[now]
    while routes:
        to = routes.pop()
        if to in nodes:
            update = True
            idx = cycle.index(to)
            cycle = cycle[:i+1] + cycle[idx:]
            nodes = set(cycle)
            length = len(cycle)
            break
    i += 1

print((len(cycle)))
for node in cycle:
    print((node+1))

