t = int(input())
for _ in range(t):
    (x1, y1, x2, y2) = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    if dx == dy:
        print(dx * (dx + 1) - dx + 1)
    else:
        mid = min(dx, dy)
        mad = max(dx, dy)
        print(mid * (mid + 1) + (mad - mid - 1) * mid + 1)
