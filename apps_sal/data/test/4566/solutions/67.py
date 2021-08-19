(n, m) = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
c = [[] for _ in range(n + 1)]
for (a, b) in edges:
    c[a].append(b)
    c[b].append(a)
for i in range(1, n + 1):
    print(len(c[i]))
