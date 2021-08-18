import numpy as np
import sys
import math


def circle3p(ps):
    A = []
    B = []
    for x, y in ps:
        Ai = [x, y, 1]
        A.append(Ai)
        B.append(- x * x - y * y)
    try:
        x = np.linalg.solve(A, B)
        return x[0], x[1], x[2]
    except np.linalg.LinAlgError:
        return None


def circle2p(ps):
    xy0, xy1 = ps
    return [(xy0[0] + xy1[0]) / 2., (xy0[1] + xy1[1]) / 2., ((xy0[0] - xy1[0]) ** 2 + (xy0[1] - xy1[1]) ** 2) / 4.]


eps = 1e-7


def main():
    N = int(sys.stdin.readline())
    ps = []
    for i in range(N):
        x, y = list(map(int, sys.stdin.readline().split()))
        ps.append((x, y))

    n = len(ps)
    ok = False
    res = int(1e9)

    if n == 2:
        x0, y0 = ps[0]
        x1, y1 = ps[1]
        print(('%.9f' % (math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) / 2.)))
        return

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                circle = circle3p([ps[i], ps[j], ps[k]])
                if circle is None:
                    continue
                a, b, c = circle
                for l in range(n):
                    if l in {i, j, k}:
                        continue
                    x, y = ps[l]
                    if x * x + y * y + a * x + b * y + c > eps:
                        break
                else:
                    res = min(res, a * a / 4 + b * b / 4 - c)

    for i in range(n):
        for j in range(i + 1, n):
            circle = circle2p([ps[i], ps[j]])
            if circle is None:
                continue
            a, b, c = circle
            for l in range(n):
                if l in {i, j}:
                    continue
                x, y = ps[l]
                if (x - a) ** 2 + (y - b) ** 2 > c + eps:
                    break
            else:
                res = min(res, c)

    print(('%.9f' % float(math.sqrt(float(res)))))


def __starting_point():
    main()


__starting_point()
