from bisect import bisect_left
import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]

    Xs = []
    Ys = []
    for x, y in XY:
        Xs.append(x)
        Ys.append(y)
    Xs.sort()
    Ys.sort()
    points = [[0 for _ in range(N)] for _ in range(N)]

    for x, y in XY:
        ix = bisect_left(Xs, x)
        iy = bisect_left(Ys, y)
        points[ix][iy] += 1

    sumpoints = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for ix in range(1, N+1):
        s = 0
        for iy in range(1, N+1):
            if ix == 1:
                sumpoints[ix][iy] = points[ix-1][iy-1]
            if points[ix-1][iy-1] == 1:
                s = 1
            sumpoints[ix][iy] = sumpoints[ix-1][iy] + s

    ans = int(8E18)
    for lx in range(N-1):
        for rx in range(lx+1, N):
            for ly in range(N-1):
                for ry in range(ly+1, N):
                    if sumpoints[rx+1][ry+1] - sumpoints[rx+1][ly] - sumpoints[lx][ry+1] + sumpoints[lx][ly] >= K:
                        s = (Xs[rx]-Xs[lx])*(Ys[ry]-Ys[ly])
                        ans = min(ans, s)
    print(ans)

def __starting_point():
    main()
__starting_point()
