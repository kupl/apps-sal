(n, A, B) = map(int, input().split())
z = [tuple(map(int, input().split())) for _ in range(n)]
inf = 10 ** 18
d = {(0, 0): 0}
for (a, b, cost) in z:
    newd = []
    for ((x, y), c) in d.items():
        new = (a + x, b + y)
        if new not in d or d[new] > c + cost:
            newd.append((new, c + cost))
    for (new, newc) in newd:
        d[new] = newc
ans = inf
for i in range(1, 10 * n):
    t = (A * i, B * i)
    if t in d:
        ans = min(ans, d[t])
if ans == inf:
    print(-1)
else:
    print(ans)
