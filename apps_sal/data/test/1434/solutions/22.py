n = int(input())
deg2vs = {}
ss = [0] * n
degs = [0] * n
for i in range(n):
    degs[i], ss[i] = list(map(int, input().split()))
    if degs[i] > 0:
        if degs[i] not in deg2vs:
            deg2vs[degs[i]] = set()
        deg2vs[degs[i]].add(i)
edges = []
while len(deg2vs) != 0:
    leaves = deg2vs.pop(1)
    for leaf in leaves:
        if degs[leaf] == 0:
            continue
        v = ss[leaf]
        edges.append((leaf, v))
        v_deg = degs[v]
        if v_deg > 1:
            deg2vs[v_deg].remove(v)
            if len(deg2vs[v_deg]) == 0:
                deg2vs.pop(v_deg)

        ss[v] = ss[v] ^ leaf
        degs[v] -= 1
        if degs[v] > 0:
            if degs[v] not in deg2vs:
                deg2vs[degs[v]] = set()
            deg2vs[degs[v]].add(v)
print(len(edges))
for edge in edges:
    print(edge[0], edge[1])
