def solve(a,b):
	n = len(a)
	m = len(b)

	a = sorted(a)
	b = sorted(b)
	r1 = n * 3
	r2 = m * 3

	max1 = r1
	max2 = r2

	p1 = 0
	p2 = 0
	while p1 < n or p2 < m:
		v = 0
		if p2 == m:
			v = a[p1]
		elif p1 == n:
			v = b[p2]
		else:
			v =min(a[p1],b[p2])

		while p1 < n and a[p1] == v:
			r1 -= 1
			p1 += 1

		while p2 < m and b[p2] == v:
			r2 -= 1
			p2 += 1

		if r1 - r2 > max1 - max2 or (r1-r2 == max1-max2 and r1 > max1):
			max1 = r1
			max2 = r2

	return (max1, max2)

n = input()
a = list(map(int, input().split(' ')))
n = input()
b = list(map(int, input().split(' ')))

print('%s:%s' % solve(a,b))


