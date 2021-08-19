(n, k) = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort()
ans = 10 ** 20
for i in range(n):
    for j in range(i, n):
        xy_tmp = xy[i:j + 1]
        if len(xy_tmp) >= k:
            l1 = xy_tmp[0][0]
            r1 = xy_tmp[-1][0]
            xy_tmp.sort(key=lambda x: x[1])
            for jj in range(len(xy_tmp) - k + 1):
                ans = min(ans, (r1 - l1) * (xy_tmp[k + jj - 1][1] - xy_tmp[jj][1]))
print(ans)
