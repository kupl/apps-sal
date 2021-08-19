(n, h, m) = [int(item) for item in input().split()]
x = [h ** 2 for _ in range(n)]
for _ in range(m):
    (l, r, xi) = [int(item) for item in input().split()]
    for u in range(l - 1, r):
        x[u] = min(xi ** 2, x[u])
print(sum(x))
