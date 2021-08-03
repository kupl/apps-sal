import sys
from itertools import combinations
from math import sqrt

read = sys.stdin.read
readline = sys.stdin.readline


def main():
    N, K, *xyc = map(int, read().split())
    x = xyc[::3]
    y = xyc[1::3]
    xy = list(zip(x, y))
    c = xyc[2::3]
    left = 0
    right = 10 ** 6
    delta = 0.1 ** 7
    while right - left > delta:
        mid = (left + right) / 2
        intersections = []
        r = [(mid / i) ** 2 for i in c]
        for i, j in combinations(range(N), 2):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            X = x2 - x1
            Y = y2 - y1
            XY = X ** 2 + Y ** 2
            r1 = r[i]
            r2 = r[j]

            a = (XY + r1 - r2) / 2
            b = XY * r1 - a ** 2
            if b < delta:
                continue
            b = sqrt(b)
            xi1 = (a * X + Y * b) / XY + x1
            yi1 = (a * Y - X * b) / XY + y1
            xi2 = (a * X - Y * b) / XY + x1
            yi2 = (a * Y + X * b) / XY + y1
            intersections.append((xi1, yi1))
            intersections.append((xi2, yi2))

        intersections.extend(xy)
        cnt = 0
        for X, Y in intersections:
            tmp = 0
            for (i, j), k in zip(xy, r):
                XY = (X - i) ** 2 + (Y - j) ** 2
                if XY < k + delta:
                    tmp += 1
            cnt = max(tmp, cnt)
            if cnt >= K:
                break
        if cnt >= K:
            right = mid
        else:
            left = mid

    print(right)


def __starting_point():
    main()


__starting_point()
