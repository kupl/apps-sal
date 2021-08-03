import math
N = int(input())
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy += [(x, y, math.atan2(y, x))]
xy.sort(key=lambda val: val[2])
x_accum = [0]
y_accum = [0]
for i in range(N):
    x_accum += [x_accum[-1] + xy[i][0]]
    y_accum += [y_accum[-1] + xy[i][1]]

ans = 0
for i in range(N + 1):
    for j in range(i, N + 1):
        ans = max(ans, math.hypot(x_accum[j] - x_accum[i], y_accum[j] - y_accum[i]))
        ans = max(ans, math.hypot(x_accum[-1] - x_accum[j] + x_accum[i], y_accum[-1] - y_accum[j] + y_accum[i]))
print(ans)
