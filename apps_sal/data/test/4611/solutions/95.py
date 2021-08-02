n = int(input())
pt, px, py = 0, 0, 0

for _ in range(n):
    ct, cx, cy = map(int, input().split())
    t = ct - pt
    d = abs(cx - px) + abs(cy - py)
    if t < d or (t % 2) != (d % 2):
        print('No')
        break
    pt, px, py = ct, cx, cy
else:
    print('Yes')
