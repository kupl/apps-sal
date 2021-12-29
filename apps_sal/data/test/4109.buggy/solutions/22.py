(n, m, x) = map(int, input().split())
c = list((list(map(int, input().split())) for _ in range(n)))
ans = 10 ** 7
for i in range(1 << n):
    mokuhyo = [0] * m
    cost = 0
    for j in range(n):
        if i >> j & 1:
            for r in range(m):
                mokuhyo[r] += c[j][r + 1]
            cost += c[j][0]
    if all((k >= x for k in mokuhyo)):
        ans = min(ans, cost)
print('-1' if ans == 10 ** 7 else ans)
