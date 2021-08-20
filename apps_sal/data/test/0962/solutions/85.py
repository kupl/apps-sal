def cycle_detection(V, E, s):
    prev = [-1] * len(V)
    stack = [s]
    while stack:
        v = stack.pop()
        for u in E[v]:
            if u == s:
                prev[u] = v
                return (s, prev)
            if prev[u] == -1:
                stack.append(u)
                prev[u] = v
    return (-1, prev)


(N, M) = map(int, input().split())
V = list(range(N))
E = [[] for _ in range(N)]
edges = []
for _ in range(M):
    (a, b) = map(int, input().split())
    E[a - 1].append(b - 1)
    edges.append((a - 1, b - 1))
dag = False
for v in range(N):
    (s, prev) = cycle_detection(V, E, v)
    if s != -1:
        break
else:
    dag = True
if dag:
    print(-1)
else:
    cycle = set()
    cycle.add(s)
    pv = prev[s]
    while pv != s:
        cycle.add(pv)
        pv = prev[pv]
    for (a, b) in edges:
        if a in cycle and b in cycle and (prev[b] != a):
            pv = prev[b]
            while pv != a:
                cycle.remove(pv)
                pv = prev[pv]
            prev[b] = a
    print(len(cycle))
    print(*[v + 1 for v in cycle], sep='\n')
