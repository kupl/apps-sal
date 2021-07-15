import sys
def input():
	return sys.stdin.readline()[:-1]

INF = 10**30
n = int(input())
p = [input().split() for _ in range(n)]

"""
[0]: max or min / for
[1]: max or min / against
[2]: max or min / fixed
"""

r = [-INF, -INF, -INF]
l = [INF, INF, INF]
u = [-INF, -INF, -INF]
d = [INF, INF, INF]

for x, y, t in p:
	x, y = int(x), int(y)
	if t == "R":
		r[0] = max(r[0], x)
		l[1] = min(l[1], x)
		u[2] = max(u[2], y)
		d[2] = min(d[2], y)
	elif t == "L":
		r[1] = max(r[1], x)
		l[0] = min(l[0], x)
		u[2] = max(u[2], y)
		d[2] = min(d[2], y)
	elif t == "U":
		r[2] = max(r[2], x)
		l[2] = min(l[2], x)
		u[0] = max(u[0], y)
		d[1] = min(d[1], y)
	else:
		r[2] = max(r[2], x)
		l[2] = min(l[2], x)
		u[1] = max(u[1], y)
		d[0] = min(d[0], y)

#print(r)
#print(l)
#print(u)
#print(d)

timings = set([0])

if r[0] <= r[1] <= r[2]:
	timings.add(abs(r[2]-r[0]))
elif r[0] <= r[2] <= r[1]:
	timings.add(abs(r[1]-r[0])/2)
	timings.add(abs(r[2]-r[0]))
	timings.add(abs(r[1]-r[2]))
elif r[1] <= r[0] <= r[2]:
	timings.add(abs(r[2]-r[0]))
elif r[2] <= r[0] <= r[1]:
	timings.add(abs(r[1]-r[0])/2)

if l[0] >= l[1] >= l[2]:
	timings.add(abs(l[2]-l[0]))
elif l[0] >= l[2] >= l[1]:
	timings.add(abs(l[1]-l[0])/2)
	timings.add(abs(l[2]-l[0]))
	timings.add(abs(l[1]-l[2]))
elif l[1] >= l[0] >= l[2]:
	timings.add(abs(l[2]-l[0]))
elif l[2] >= l[0] >= l[1]:
	timings.add(abs(l[1]-l[0])/2)

if u[0] <= u[1] <= u[2]:
	timings.add(abs(u[2]-u[0]))
elif u[0] <= u[2] <= u[1]:
	timings.add(abs(u[1]-u[0])/2)
	timings.add(abs(u[2]-u[0]))
	timings.add(abs(u[1]-u[2]))
elif u[1] <= u[0] <= u[2]:
	timings.add(abs(u[2]-u[0]))
elif u[2] <= u[0] <= u[1]:
	timings.add(abs(u[1]-u[0])/2)

if d[0] >= d[1] >= d[2]:
	timings.add(abs(d[2]-d[0]))
elif d[0] >= d[2] >= d[1]:
	timings.add(abs(d[1]-d[0])/2)
	timings.add(abs(d[2]-d[0]))
	timings.add(abs(d[1]-d[2]))
elif d[1] >= d[0] >= d[2]:
	timings.add(abs(d[2]-d[0]))
elif d[2] >= d[0] >= d[1]:
	timings.add(abs(d[1]-d[0])/2)

#print(timings)
ans = 10**30
for t in timings:
	if t > 10**10:
		continue
	R, L, U, D = -INF, INF, -INF, INF
	for x, y, di in p:
		if di == "R":
			x, y = int(x)+t, int(y)
		elif di == "L":
			x, y = int(x)-t, int(y)
		elif di == "U":
			x, y = int(x), int(y)+t
		else:
			x, y = int(x), int(y)-t

		R = max(R, x)
		L = min(L, x)
		U = max(U, y)
		D = min(D, y)

	ans = min(ans, (R-L)*(U-D))

print(ans)
