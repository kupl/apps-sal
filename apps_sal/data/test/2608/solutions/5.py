def area(rect):
    if rect is None:
        return 0
    (x1, y1, x2, y2) = rect
    return (x2 - x1 + 1) * (y2 - y1 + 1)


def get_w(rect):
    if rect is None:
        return 0
    (x1, y1, x2, y2) = rect
    ra = area(rect)
    (more, less) = ((ra + 1) // 2, ra // 2)
    if (x1 + y1) % 2 == 0:
        return more
    else:
        return less


def intersect_rects(r1, r2):
    out = []
    for (i, a, b) in zip(list(range(4)), r1, r2):
        out.append(max(a, b) if i < 2 else min(a, b))
    if out[0] > out[2] or out[1] > out[3]:
        return None
    return out


def main():
    (n, m) = list(map(int, input().split()))
    rect1 = list(map(int, input().split()))
    rect2 = list(map(int, input().split()))
    rect12 = intersect_rects(rect1, rect2)
    w_start = get_w([1, 1, n, m])
    w1 = get_w(rect1)
    w2 = get_w(rect2)
    w12 = get_w(rect12)
    w = w_start - w1 - w2 + w12 + area(rect1) - area(rect12)
    print(w, n * m - w)


q = int(input())
for i in range(q):
    main()
