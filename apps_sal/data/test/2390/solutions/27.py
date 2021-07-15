import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, c = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(n)]
    R1, R2 = [0], [0]
    max1, max2 = [0], [0]
    ma = 0
    prev = 0
    for x, y in XY:
        R1.append(R1[-1] + y - (x - prev))
        prev = x
        if ma < R1[-1]:
            ma = R1[-1]
        max1.append(ma)

    ma = 0
    prev = 0
    for x, y in XY[::-1]:
        R2.append(R2[-1] + y - ((c - x) - prev))
        prev = (c - x)
        if ma < R2[-1]:
            ma = R2[-1]
        max2.append(ma)

    res = max(max(R1), max(R2))
    for i in range(1, n + 1):
        point1 = R1[i] - XY[i - 1][0] + max2[n - i]
        point2 = R2[i] - (c - XY[-i][0]) + max1[n - i]
        res = max(res, point1, point2)
    print(res)


def __starting_point():
    resolve()

__starting_point()
