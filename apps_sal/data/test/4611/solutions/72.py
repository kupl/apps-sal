n = int(input())
px = py = pt = 0
for i in range(n):
	t,x,y = map(int,input().split())
	d = abs(x - px) + abs(y - py)
	nt = t - pt
	if nt < d or d%2 != nt%2:
		print("No")
		return
	px = x
	py = y
	pt = t
print("Yes")
