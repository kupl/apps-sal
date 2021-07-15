ax, ay, bx, by, cx, cy = map(int, input().split())
ux = cx - bx
uy = cy - by
vx = bx - ax
vy = by - ay

if uy*vx == vy*ux or ux**2 + uy**2 != vx**2 + vy**2:
	print("No") 
else:
	print("Yes")
