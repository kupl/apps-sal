N, K, *XY = [int(_) for _ in open(0).read().split()]
XY = sorted(zip(XY[::2], XY[1::2]))
ans = float('inf')
for i in range(N):
    for j in range(i + K - 1, N):
        xlen = XY[j][0] - XY[i][0]
        Y = sorted(y for x, y in XY[i:j + 1])
        ylen = min(y2 - y1 for y1, y2 in zip(Y, Y[K - 1:]))
        ans = min(ans, xlen * ylen)
print(ans)
