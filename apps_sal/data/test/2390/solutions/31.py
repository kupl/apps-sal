from itertools import accumulate


N, C, *xv = list(map(int, open(0).read().split()))
xv = [(x, v) for x, v in zip(*[iter(xv)] * 2)]

cw_acc = [0] * (N + 1)
ccw_acc = [0] * (N + 1)
cw_prev = 0
ccw_prev = C
for i in range(N):
    k = N - i - 1
    cw_acc[i + 1] = cw_acc[i] + xv[i][1] - (xv[i][0] - cw_prev)
    cw_prev = xv[i][0]
    ccw_acc[i + 1] = ccw_acc[i] + xv[k][1] - (ccw_prev - xv[k][0])
    ccw_prev = xv[k][0]

cw_acc = list(accumulate(cw_acc, max))
ccw_acc = list(accumulate(ccw_acc, max))
ans = 0
for i in range(N):
    k = N - i - 1
    ans = max(
        ans,
        cw_acc[i + 1],
        cw_acc[i + 1] - xv[i][0] + ccw_acc[k],
        ccw_acc[i + 1],
        ccw_acc[i + 1] - (C - xv[k][0]) + cw_acc[k],
    )
print(ans)

