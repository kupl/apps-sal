#!/usr/bin/env python3

import bisect

[n, q] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))
kis = list(map(int, input().strip().split()))

iais = [0 for _ in range(n + 1)]
for i in range(n):
	iais[i + 1] = iais[i] + ais[i]


def bsearch(v, xmin, xmax):
	while xmax - xmin > 1:
		xmid = (xmin + xmax) // 2
		if v >= iais[xmid]:
			xmin = xmid
		else:
			xmax = xmid
	return xmin

def lsearch(v, xmin, xmax):
	x = xmin
	while x + 1 < xmax and v >= iais[x + 1]:
		x += 1
	return x

thrs = (iais[-1] // n + 1) * 440



s = 0
tot = iais[-1]
prevr = 0
for k in kis:
	s += k
	if s >= tot:
		print (n)
		s = 0
		prevr = 0
	else:
		r = bisect.bisect_right(iais, s, prevr) - 1
		print(n - r)
		prevr = r


