k = int(input())
x, y = map(int, input().split())

def sign(x):
    return 1 if x > 0 else -1

if (abs(x) + abs(y)) % 2 == 1 and k % 2 == 0:
    print(-1)
else:
    cx, cy = 0, 0
    ret = []
    while x != cx or y != cy:
        if abs(x - cx) + abs(y - cy) == k:
            cx, cy = x, y
        elif abs(x - cx) + abs(y - cy) <= 2 * k:
            dx = abs(x - cx)
            dy = abs(y - cy)
            rem = 2 * k - dx - dy
            if dx > dy:
                cy += (dy + rem // 2) * sign(y - cy)
                cx += (k - dy - rem // 2) * sign(x - cx)
            else:
                cx += (dx + rem // 2) * sign(x - cx)
                cy += (k - dx - rem // 2) * sign(y - cy)
        else:
            if abs(x - cx) > abs(y - cy):
                cx += sign(x - cx) * k
            else:
                cy += sign(y - cy) * k
        ret.append((cx, cy))

    print(len(ret))
    for cx, cy in ret:
        print(cx, cy)
