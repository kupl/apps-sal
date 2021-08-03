N, K = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(N)]


xy.sort()
ans = 2000000000 * (xy[-1][0] - xy[0][0])
for i in range(K - 1, N):
    for j in range(N - i):
        xnow = xy[j + i][0] - xy[j][0]
        ylst = [xy[k][1] for k in range(j, j + i + 1)]
        ylst.sort()
        ynow = min([ylst[k + K - 1] - ylst[k] for k in range(i + 2 - K)])
        ans = min(ans, xnow * ynow)

print(ans)
