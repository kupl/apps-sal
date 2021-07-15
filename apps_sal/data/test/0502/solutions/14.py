ax, ay, bx, by, cx, cy = input().split()
ax, ay, bx, by, cx, cy = int(ax), int(ay), int(bx), int(by), int(cx), int(cy)

lAB = (bx - ax)**2 + (by - ay)**2
lBC = (cx - bx)**2 + (cy - by)**2

if lAB == lBC and (by - ay)*(cx - bx) != (cy - by)*(bx - ax):
    print("Yes")
else:
    print("No")

