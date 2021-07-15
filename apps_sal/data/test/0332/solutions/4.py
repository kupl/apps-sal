import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

n, m = mints()
z = [None,None]
for k in range(2):
	x = [[] for i in range(n+m)]
	for i in range(n):
		a = list(mints())
		for j in range(m):
			x[i+j].append(a[j])
	z[k] = x
for i in range(n+m):
	a = z[0][i]
	b = z[1][i]
	a.sort()
	b.sort()
	if a != b:
		print("NO")
		return
print("YES")

