n, m, q = map(int, input().split())
lr = []
for _ in range(m):
    lr.append(list(map(int, input().split())))

a = [[0] * n for i in range(n)]
for l, r in lr:
    a[l - 1][r - 1] += 1

cnt = [[0] * n for i in range(n)]
for y in range(n):
    v = 0
    for x in range(y, -1, -1):
        v += a[x][y]
        cnt[x][y] = cnt[x][y - 1] + v

for _ in range(q):
    p, q = map(int, input().split())
    print(cnt[p - 1][q - 1])
