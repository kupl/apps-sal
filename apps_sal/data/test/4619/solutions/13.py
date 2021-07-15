W, H, N = list(map(int, input().split()))
bl_x, tr_x, bl_y, tr_y = 0, W, 0, H
for i in range(N):
	x, y, a = list(map(int, input().split()))
	if a == 1:
		bl_x = max(bl_x, x)
	elif a == 2:
		tr_x = min(tr_x, x)
	elif a == 3:
		bl_y = max(bl_y, y)
	elif a == 4:
		tr_y = min(tr_y, y)
print((max(tr_x - bl_x, 0) * max(tr_y - bl_y, 0)))

