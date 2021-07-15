#!/usr/bin/env python3


d = int(input().strip())
[n, m] = list(map(int, input().strip().split()))
Hxds = [0 for _ in range(n)]
Hyds = [0 for _ in range(m)]
Vxds = [0 for _ in range(n)]
Vyds = [0 for _ in range(m)]
ds = []
for i in range(d):
	x1, y1, x2, y2 = list(map(int, input().strip().split()))
	if x1 == x2:
		Hxds[x1 - 1] += 1
		Hyds[min(y1, y2) - 1] += 1
		ds.append((x1 - 1, min(y1, y2) - 1, 'h'))
	else:
		Vxds[min(x1, x2) - 1] += 1
		Vyds[y1 - 1] += 1
		ds.append((min(x1, x2) - 1, y1 - 1, 'v'))
cl, cr, ct, cb = list(map(int, input().strip().split()))

if (d - 1 - cl - cr) * (d - 1 - ct - cb) > 0:
	print(-1)
	return


def makeI(xs):
	I = [0 for _ in range(len(xs) + 1)]
	for i in range(len(xs)):
		I[i + 1] = I[i] + xs[i]
	return I

def find_x_Hor(IH, IV, l, cl, cr):
	if cl + cr > d - 1:
		return -1
	x = 0
	while x <= l and (IH[x] + IV[x] < cl or d - IH[x + 1] - IV[x] > cr):
		x += 1
	if x < l and IH[x] + IV[x] == cl and (d - IH[x + 1] - IV[x]) == cr:
		return x
	return -1

def find_x_Vert(IH, IV, l, cl, cr):
	if cl + cr < d - 1:
		return -1
	x = 0
	while x < l and (IH[x + 1] + IV[x + 1] < cl + 1 or d - IH[x + 1] - IV[x] > cr + 1):
		x += 1
	if x < l and IH[x + 1] + IV[x + 1] == cl + 1 and (d - IH[x + 1] - IV[x]) == cr + 1:
		return x
	return -1
	

IHx = makeI(Hxds)
IHy = makeI(Hyds)
IVx = makeI(Vxds)
IVy = makeI(Vyds)

if ct + cb >= d - 1 and cr + cl <= d - 1:  # horizontal sofa
	x = find_x_Hor(IHx, IVx, n, cl, cr)
	y = find_x_Vert(IVy, IHy, m, ct, cb)
	if x >= 0 and y >= 0:
		if (x, y, 'h') in ds:
			print(ds.index((x, y, 'h')) + 1)
			return

if ct + cb <= d - 1 and cr + cl >= d - 1:  # vertical sofa
	x = find_x_Vert(IHx, IVx, n, cl, cr)
	y = find_x_Hor(IVy, IHy, m, ct, cb)
	if x >= 0 and y >= 0:
		if (x, y, 'v') in ds:
			print(ds.index((x, y, 'v')) + 1)
			return

print(-1)


