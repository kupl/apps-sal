import sys
ax, ay, bx, by, cx, cy = map(int, input().split())
if (ax - bx)**2 + (ay - by)**2 == (bx - cx)**2 + (by - cy)**2 and (by - ay) * (cx - bx) != (cy - by) * (bx - ax):
    print("Yes")
else:
    print("No")
