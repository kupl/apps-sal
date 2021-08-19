from sys import stdin
import math


def duh0(x1, x2, x3, x4, y1, y2, y3, y4, midonly=False):
    W = B = 0
    if (x3 <= x2) and (x1 <= x4):
        # print(1)
        w, b = duh1(max(x1, x3), min(x2, x4),
                    y1, y2, y3, y4, midonly)
        W += w
        B += b
    if midonly:
        return (W, B)

    if (x1 < x3):
        # print(3)
        w, b = duh1(x1, min(x2, x3 - 1),
                    y1, y2, y3, y4)
        W += w
        B += b
    if (x4 < x2):
        # print(7)
        w, b = duh1(max(x1, x4 + 1), x2,
                    y1, y2, y3, y4)
        W += w
        B += b
    return (W, B)


def duh1(xa, xb, y1, y2, y3, y4, midonly=False):
    W = B = 0
    if (y3 <= y2) and (y1 <= y4):
        # print("  ", 1, y1, y2, y3, y4)
        w, b = cnt(xa, xb, max(y1, y3), min(y2, y4))
        W += w
        B += b
    if midonly:
        return (W, B)

    if (y1 < y3):
        # print("  ", 4)
        w, b = cnt(xa, xb, y1, min(y2, y3 - 1))
        W += w
        B += b
    if (y4 < y2):
        # print("  ", 8)
        w, b = cnt(xa, xb, max(y1, y4 + 1), y2)
        W += w
        B += b
    return (W, B)


def cnt(xa, xb, ya, yb):
    m = xb - xa + 1
    n = yb - ya + 1
    W = m * n
    B = W // 2
    W -= B
    return (B, W) if (xa + ya) & 1 else (W, B)


def solve(n, m,
          x1, y1, x2, y2,
          x3, y3, x4, y4):
    st = cnt(1, m, 1, n)

    whi = duh0(x1, x2, x3, x4, y1, y2, y3, y4)
    its = duh0(x1, x2, x3, x4, y1, y2, y3, y4, midonly=True)
    bla = cnt(x3, x4, y3, y4)

    W = st[0] + whi[1] - its[1] - bla[0]
    B = st[1] - whi[1] + its[1] + bla[0]

    # print(st, whi, its, bla, sep="  ")

    print(W, B)


###########################
###########################


def intRead():
    while True:
        ln = stdin.readline().strip()
        if not ln:
            return
        for i in map(int, ln.split()):
            yield i


def __starting_point():
    ipt = intRead()
    t = next(ipt)
    while t:
        t -= 1
        n = next(ipt)
        m = next(ipt)
        x1 = next(ipt)
        y1 = next(ipt)
        x2 = next(ipt)
        y2 = next(ipt)
        x3 = next(ipt)
        y3 = next(ipt)
        x4 = next(ipt)
        y4 = next(ipt)
        solve(n, m,
              x1, y1, x2, y2,
              x3, y3, x4, y4)


__starting_point()
