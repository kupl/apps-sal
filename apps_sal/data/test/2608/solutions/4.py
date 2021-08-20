t = int(input())


def getcol(x1, y1, x2, y2):
    dx = max(x2 - x1 + 1, 0)
    dy = max(y2 - y1 + 1, 0)
    b = w = dx * dy // 2
    if dx % 2 and dy % 2:
        if (x1 + y1) % 2:
            b = b + 1
        else:
            w = w + 1
    return (w, b)


for _ in range(t):
    (n, m) = list(map(int, input().split()))
    (x1, y1, x2, y2) = list(map(int, input().split()))
    (x3, y3, x4, y4) = list(map(int, input().split()))
    (w, b) = getcol(1, 1, n, m)
    (w1, b1) = getcol(x1, y1, x2, y2)
    (w2, b2) = getcol(x3, y3, x4, y4)
    (w3, b3) = getcol(max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))
    woff = w - w1 - w2 + w3
    boff = b - b1 - b2 + b3
    print(woff + w1 - w3 + b1 - b3, boff + w3 + b3 + b2 - b3 + w2 - w3)
