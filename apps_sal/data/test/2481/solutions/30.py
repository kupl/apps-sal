h, w = map(int, input().split())

inf = 10 ** 20
d = [list(map(int, input().split())) for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for _ in range(h):
    row = list(map(int, input().split()))
    for num in row:
        if num == -1:
            continue
        ans += d[num][1]

print(ans)
