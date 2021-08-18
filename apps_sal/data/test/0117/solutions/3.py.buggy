#168 - F
import sys
import numpy as np
#from numba import njit


def main():
    N, M = list(map(int, sys.stdin.buffer.readline().split()))
    LineData = np.int64(sys.stdin.buffer.read().split())

    INF = 10**9 + 1

    LineData = LineData.reshape(-1, 3)
    A, B, C = LineData[:N].T
    D, E, F = LineData[N:].T
    #X = np.unique(np.concatenate([D, [-INF, 0, INF]]))
    #Y = np.unique(np.concatenate([C, [-INF, 0, INF]]))
    X = np.unique(np.concatenate([D, [-INF, INF]]))
    Y = np.unique(np.concatenate([C, [-INF, INF]]))
    A = np.searchsorted(X, A)
    B = np.searchsorted(X, B, 'right') - 1
    C = np.searchsorted(Y, C)
    D = np.searchsorted(X, D)
    E = np.searchsorted(Y, E)
    F = np.searchsorted(Y, F, 'right') - 1

    area = cal_area(A, B, C, D, E, F, X, Y)

    if area == 0:
        print("INF")
    else:
        print(area)


# @njit
def cal_area(A, B, C, D, E, F, X, Y):
    x = np.searchsorted(X, 0, 'right') - 1
    y = np.searchsorted(Y, 0, 'right') - 1

    DX = X[1:] - X[:-1]
    DY = Y[1:] - Y[:-1]

    A = A.tolist()
    B = B.tolist()
    C = C.tolist()
    D = D.tolist()
    E = E.tolist()
    F = F.tolist()
    X = X.tolist()
    Y = Y.tolist()
    DX = DX.tolist()
    DY = DY.tolist()

    LenX = len(X)
    LenY = len(Y)

    visit = [[False] * LenY for _ in range(LenX)]
    visit[x][y] = True
    area = 0
    queue = [(x, y)]

    LineX = [[False] * LenY for _ in range(LenX)]
    LineY = [[False] * LenY for _ in range(LenX)]

    # for x1, x2, y in zip(A, B, C):
    #    for x in range(x1, x2):
    #        LineY[x][y] = True
    for i in range(len(A)):
        y = C[i]
        for x in range(A[i], B[i]):
            LineY[x][y] = True

    # for x, y1, y2 in zip(D, E, F):
    #    for y in range(y1, y2):
    #        LineX[x][y] = True
    for i in range(len(D)):
        x = D[i]
        for y in range(E[i], F[i]):
            LineX[x][y] = True

    LenX -= 1
    LenY -= 1

    while queue:
        x, y = queue.pop()

        if x == 0 or x == LenX or y == 0 or y == LenY:
            area = 0
            break

        area += DX[x] * DY[y]

        if not LineX[x][y] and not visit[x - 1][y]:
            visit[x - 1][y] = True
            queue.append((x - 1, y))
        if not LineY[x][y] and not visit[x][y - 1]:
            visit[x][y - 1] = True
            queue.append((x, y - 1))
        if not LineX[x + 1][y] and not visit[x + 1][y]:
            visit[x + 1][y] = True
            queue.append((x + 1, y))
        if not LineY[x][y + 1] and not visit[x][y + 1]:
            visit[x][y + 1] = True
            queue.append((x, y + 1))

    return area


def __starting_point():
    main()


return

__starting_point()
