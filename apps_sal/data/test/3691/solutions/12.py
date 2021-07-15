def dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])
x0, y0, ax, ay, bx, by = [int(i) for i in input().split()]
xs, ys, t = [int(i) for i in input().split()]
a = [[x0, y0]]
for i in range(64):
	a.append([a[-1][0] * ax + bx, a[-1][1] * ay + by])
ans = 0
for l in range(len(a)):
	for r in range(len(a)):
		if dist([xs, ys], a[l]) + dist(a[l], a[r]) <= t:
			ans = max(ans, abs(r - l) + 1)
print(ans)
