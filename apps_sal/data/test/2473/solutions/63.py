(n, k) = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]
ary.sort()
ans = float('Inf')
for i in range(n - k + 1):
    for j in range(k, n - i + 1):
        xmin = ary[i][0]
        xmax = ary[i + j - 1][0]
        ary_y = sorted(ary[i:i + j], key=lambda x: x[1])
        for l in range(len(ary_y) - k + 1):
            ymin = ary_y[l][1]
            ymax = ary_y[l + k - 1][1]
            ans = min(ans, (xmax - xmin) * (ymax - ymin))
print(ans)
