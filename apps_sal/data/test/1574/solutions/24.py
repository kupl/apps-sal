(n, m) = list(map(int, input().split()))
Es = [set() for i in range(n)]
edges = set()
for i in range(m):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    Es[a].add(b)
    Es[b].add(a)
    edges.add((a, b))
record = float('inf')
for (a, b) in edges:
    cost_a = len(Es[a]) - 2
    cost_b = len(Es[b]) - 2
    cost = cost_a + cost_b
    if cost >= record:
        continue
    if cost_a > cost_b:
        (a, b) = (b, a)
    for c in Es[a]:
        cost_abc = cost + len(Es[c]) - 2
        if b in Es[c]:
            if cost_abc < record:
                record = cost_abc
if record == float('inf'):
    print(-1)
else:
    print(record)
