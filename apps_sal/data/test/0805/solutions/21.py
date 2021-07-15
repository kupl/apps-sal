import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n = mint()
a = []
for i in range(n):
	a.append(tuple(mints()))
r = 0
for i in range(*a[0]):
	r += 1
	for j in range(1,len(a)):
		z = a[j]
		if z[0]<=i and z[1]>i:
			r -= 1
			break
print(r)
