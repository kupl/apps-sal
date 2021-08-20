n = int(input())
a = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for u in range(1, n):
    (p, c) = (int(x) for x in input().split())
    g[p - 1].append((u, c))
stack = [(0, 0, False)]
r = 0
while stack:
    (u, d, f) = stack.pop()
    f = f or d > a[u]
    if f:
        r += 1
    for (v, c) in g[u]:
        stack.append((v, d + c if d + c >= 0 else 0, f))
print(r)
