#!/usr/bin/env python3

from array import array

k = int(input().strip())
s = input().strip()

n = len(s)

# first True
def bsearch(f, xmin, xmax):
	while xmax - xmin > 1:
		xmid = (xmax + xmin) // 2
		if f(xmid):
			xmax = xmid
		else:
			xmin = xmid
	return xmax

wraps = array('l', (0 for _ in range(n)))
for i in range(1, n):
	if s[i - 1] == ' ' or s[i - 1] == '-':
		wraps[i] = i
	else:
		wraps[i] = wraps[i - 1] 
		

def f(l):
	proc = 0
	for i in range(k):
		if proc + l >= n:
			return True
		proc = wraps[proc + l]
	return False

lmin = max(i - w for i, w in enumerate(wraps))
lmin = max(lmin, (n - 1) // k)

lmax = n

l = bsearch(f, lmin, lmax)

print (l)

