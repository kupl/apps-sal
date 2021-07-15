ax, ay, bx, by, cx, cy = map(int, input().split())
Bab = ax - bx
Aab = by - ay
Cab = -1 * Aab * ax - Bab * ay
if Aab * cx + Bab * cy + Cab == 0:
    print("No")
else:
    ab = (ax - bx) ** 2 + (ay - by) ** 2
    ac = (ax - cx) ** 2 + (ay - cy) ** 2
    bc = (by - cy) ** 2 + (bx - cx) ** 2
    if ab == bc:
        print("Yes")
    else:
        print("No")
