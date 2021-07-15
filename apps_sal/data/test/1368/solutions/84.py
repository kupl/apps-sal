import math
n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
c = 0
def comb(N, R):
	if N < R:
		return 0
	return math.factorial(N) // (math.factorial(N - R) * math.factorial(R))
if len(set(v[:a])) == 1:
	x = v[:a][0]
	d = 0
	for i in v:
		if i == x:
			d += 1
	for i in range(a,min(d+1,b+1)):
		c += comb(d,i)
	print (x)
	print (c)
else:
	x = v[:a][0]
	y = sorted(v[:a])
	av = sum(v[:a])/a
	z = y[0]
	d = 0
	for i in v:
		if i == z:
			d += 1
	e = 0
	for i in y:
		if i == z:
			e += 1
	c = comb(d,e)
	print (av)
	print (c)
