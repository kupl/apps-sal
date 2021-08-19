def dfs(v, visited, edges, colors):
    st = [v]
    visited.add(v)
    comp = []
    cols = dict()
    while st:
        ver = st.pop()
        comp.append(colors[ver])
        if ver in edges:
            for i in edges[ver]:
                if i not in visited:
                    st.append(i)
                    visited.add(i)
    for i in comp:
        if i not in cols:
            cols[i] = 1
        else:
            cols[i] += 1
    max_c = 0
    for i in cols:
        if cols[i] > max_c:
            max_c = cols[i]
    return len(comp) - max_c


(n, m, k) = [int(x) for x in input().split()]
colors = {i + 1: int(x) for (i, x) in enumerate(input().split())}
edges = dict()
for i in range(m):
    (v1, v2) = [int(x) for x in input().split()]
    if v1 in edges:
        edges[v1].append(v2)
    else:
        edges[v1] = [v2]
    if v2 in edges:
        edges[v2].append(v1)
    else:
        edges[v2] = [v1]
visited = set()
answer = 0
for i in range(1, n + 1):
    if i not in visited:
        answer += dfs(i, visited, edges, colors)
print(answer)
