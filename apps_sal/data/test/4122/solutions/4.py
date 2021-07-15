import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

H, n = mints()
d = list(mints())
s = [0]*(n+1)
for i in range(n):
	s[i+1] = s[i]+d[i]
for i in range(n+1):
	if s[i] + H <= 0:
		print(i)
		return
#print(s)
if s[n] >= 0:
	print(-1)
else:
	l = -1
	r = H//(-s[n]) + 2
	while r-l > 1:
		c = (l+r)//2
		h = -c*s[n]-H
		z = -1
		for i in range(n+1):
			if s[i] <= h:
				z = i
				break
		if z == -1:
			l = c
		else:
			r = c
	h = -r*s[n]-H
	z = -1
	for i in range(n+1):
		if s[i] <= h:
			print(r*n+i)
			break

