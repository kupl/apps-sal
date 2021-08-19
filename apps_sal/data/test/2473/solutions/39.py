from itertools import accumulate
from operator import add
(N, K) = list(map(int, input().split()))
(xs, ys) = ([], [])
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)
iXs = list(range(N))
iXs.sort(key=lambda iX: xs[iX])
odrXs = [0] * N
for (odrX, iX) in enumerate(iXs):
    odrXs[iX] = odrX
iYs = list(range(N))
iYs.sort(key=lambda iY: ys[iY])
odrYs = [0] * N
for (odrY, iY) in enumerate(iYs):
    odrYs[iY] = odrY
Ass = [[0] * N for _ in range(N)]
for (odrX, odrY) in zip(odrXs, odrYs):
    Ass[odrX][odrY] = 1


def getAccAss(Ass):
    accAss = [[0] * (len(Ass[0]) + 1)] + [accumulate([0] + As) for As in Ass]
    for x in range(1, len(accAss)):
        accAss[x] = list(map(add, accAss[x], accAss[x - 1]))
    return accAss


def getRangeSum2D(accAss, xFr, xTo, yFr, yTo):
    return accAss[xTo + 1][yTo + 1] - accAss[xTo + 1][yFr] - accAss[xFr][yTo + 1] + accAss[xFr][yFr]


accAss = getAccAss(Ass)
ans = 10 ** 20
for xFr in range(N - 1):
    for xTo in range(xFr + 1, N):
        for yFr in range(N - 1):
            for yTo in range(yFr + 1, N):
                num = getRangeSum2D(accAss, xFr, xTo, yFr, yTo)
                if num >= K:
                    area = (xs[iXs[xTo]] - xs[iXs[xFr]]) * (ys[iYs[yTo]] - ys[iYs[yFr]])
                    ans = min(ans, area)
print(ans)
