from collections import defaultdict

V, E = input().split()
V, E = int(V), int(E)
G = defaultdict(set)
for _ in range(E):
    v1, v2 = input().split()
    v1, v2 = int(v1), int(v2)
    G[v1].add(v2)
    G[v2].add(v1)

cycle_cnt = 0
visited = set()
for v in G:
    if v in visited:
        continue
    stack = [v]
    path = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        stack.extend(G[node])
    ok = True
    for node in path:
        if len(G[node]) != 2:
            ok = False
            break
    cycle_cnt += ok
print(cycle_cnt)
