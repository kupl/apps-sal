L = int(input())
v = list(map(int, bin(L)[:2:-1]))
N = len(v) + 1
edges = []
unit = 1
for i in range(N - 1):
    L -= unit * v[i]
    edges.append((i + 1, i + 2, 0))
    edges.append((i + 1, i + 2, unit))
    if v[i]:
        edges.append((i + 1, N, L))
    unit *= 2
print(N, len(edges))
for (a, b, c) in edges:
    print(a, b, c)
