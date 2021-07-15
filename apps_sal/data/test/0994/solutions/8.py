n, m = list(map(int, input().split(' ')))
l = [list(map(int, input().split(' '))) for _ in range(m)]

ans = max(l[0][0] + l[0][1] - 1, n - l[-1][0] + l[-1][1])

for i in range(1, m):
    dd, dh = abs(l[i][0] - l[i - 1][0]), abs(l[i][1] - l[i - 1][1])
    if dd < dh:
        print('IMPOSSIBLE')
        return
    ans = max(ans, max(l[i][1], l[i - 1][1]) + ((dd - dh) >> 1))

print(ans)

