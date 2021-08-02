H, W, N, *a = map(int, open(0).read().split())
ans = [[0] * W for _ in range(H)]
count = 0
using = 0
for i in range(H * W):
    dm = divmod(i, W)
    h = dm[0]
    if h % 2 == 0:
        w = dm[1]
    else:
        w = (dm[1] + 1) * (-1)
    ans[h][w] = using + 1
    count += 1
    if count == a[using]:
        using += 1
        count = 0
for x in ans:
    print(*x)
