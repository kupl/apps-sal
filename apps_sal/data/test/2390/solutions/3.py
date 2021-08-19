(N, C) = list(map(int, input().split()))
xv = [list(map(int, input().split())) for _ in range(N)]
xinc = [0] * N
xinc2 = [0] * N
xdec = [0] * N
xdec2 = [0] * N
nowx = 0
nowv = 0
nowxin = C
nowvin = 0
for i in range(N):
    (xi, vi) = xv[i]
    nowv = nowv - (xi - nowx) + vi
    xinc[i] = nowv
    xinc2[i] = nowv - xi
    nowx = xi
    (xin, vin) = xv[N - 1 - i]
    nowvin = nowvin - (nowxin - xin) + vin
    xdec[i] = nowvin
    xdec2[i] = nowvin - (C - xin)
    nowxin = xin
mxinc2 = [0] * N
mxdec2 = [0] * N
for i in range(1, N):
    mxinc2[i] = max(mxinc2[i - 1], xinc2[i - 1])
    mxdec2[i] = max(mxdec2[i - 1], xdec2[i - 1])
ans = 0
for i in range(N):
    ans = max(ans, xinc[i], xdec[i])
    ans = max(ans, mxinc2[i] + xdec[N - 1 - i])
    ans = max(ans, mxdec2[i] + xinc[N - 1 - i])
print(ans)
