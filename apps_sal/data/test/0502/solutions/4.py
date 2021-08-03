from math import sqrt

ax, ay, bx, by, cx, cy = [int(i) for i in input().split()]
if (ax - bx)**2 + (ay - by)**2 != (bx - cx)**2 + (by - cy)**2:
    print("No")
elif abs((ax - bx) * (bx - cx) + ((ay - by) * (by - cy)))**2 == ((ax - bx)**2 + (ay - by)**2) * ((bx - cx)**2 + (by - cy)**2):
    print("No")
else:
    print("Yes")
