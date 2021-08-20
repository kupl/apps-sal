(n, m, x) = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
ans = 12 * 10 ** 5 + 1
for i in range(2 ** n):
    kingaku = 0
    rikaido = [0] * m
    for j in range(n):
        if i >> j & 1:
            kingaku += books[j][0]
            for k in range(m):
                rikaido[k] += books[j][k + 1]
    if all((a >= x for a in rikaido)):
        ans = min(ans, kingaku)
if ans != 12 * 10 ** 5 + 1:
    print(ans)
else:
    print('-1')
