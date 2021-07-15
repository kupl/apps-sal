n, x = list(map(int, input().split()))

bad = 0

for i in range(n):
	l = input().split()
	cmd, d = l
	d = int(d)
	if cmd == '+':
		x += d
	else:
		if x >= d:
			x -= d
		else:
			bad += 1

print(x, bad)

