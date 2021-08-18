import sys
fin = sys.stdin

n = int(fin.readline())
p = []
for i in range(n):
    a, b, c, d = map(int, fin.readline().split())
    p += [((a, b), (c, d))]


def width(rect):
    return rect[1][0] - rect[0][0]


def height(rect):
    return rect[1][1] - rect[0][1]


def square(rect):
    return width(rect) * height(rect)


def squareOfRects(rects):
    return sum(square(r) for r in rects)


def left(rects):
    return min(r[0][0] for r in rects)


def right(rects):
    return max(r[1][0] for r in rects)


def bottom(rects):
    return min(r[0][1] for r in rects)


def top(rects):
    return max(r[1][1] for r in rects)


def isSquare(rects):
    w, h = right(rects) - left(rects), top(rects) - bottom(rects)
    return w == h and squareOfRects(rects) == w * h


print("YES" if isSquare(p) else "NO")
