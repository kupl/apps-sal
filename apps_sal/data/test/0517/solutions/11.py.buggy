n, d, h = map(int, input().split())

if n == 2 and d == h == 1:
    print(1, 2)
    return

if d == h == 1:
    print(-1)
    return

if d > 2 * h:
    print(-1)
    return

flow = 0
edges = []
for i in range(h):
    edges.append((i + 1, i + 2))

last = 1
for i in range(d - h):
    edges.append((last, len(edges) + 2))
    last = edges[-1][1]
if d == h:
    m = 2
else:
    m = 1
i = d + 2
while len(edges) < n - 1:
    edges.append((m, i))
    i += 1
for edge in edges:
    print(*edge)
