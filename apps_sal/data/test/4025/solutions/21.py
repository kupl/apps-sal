a, b, c = map(int, input().split())
sa, sb, sc = a // 3, b // 2, c // 2
m = min(sa, sb, sc)
pa, pb, pc = a - 3 * m, b - 2 * m, c - 2 * m
d = [1,2,3,1,3,2,1,1,2,3,1,3,2,1,1,2,3,1,3,2,1]
mr = 0
for i in range(7):
	a,b,c = pa, pb, pc
	k = i
	r = 0
	while not -1 in [a,b,c]:
		if d[k] == 1:
			a -= 1
		elif d[k] == 2:
			b -= 1
		else:
			c -= 1
		k += 1
		r += 1
	mr = max(r, mr)
print(7 * m + mr - 1)
