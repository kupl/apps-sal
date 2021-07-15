3

x1, y1, x2, y2 = [int(i) for i in input().split()]

dx = x2 - x1 + 1
dy = (y2 - y1) // 2 + 1

if dx%2 == 1:
	ans = dy * (dx//2 + 1) + (dy-1) * (dx//2)
else:
	ans = dx*dy

print(ans)

