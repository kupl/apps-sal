import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

n = mint()
q = list(mints())
a = [0]*n
for i in range(0,n-1):
	a[i+1] = a[i] + q[i]
m = min(a)
for i in range(n):
	a[i] -= m - 1
if max(a) != n or len(set(a)) != n:
	print(-1)
else:
	print(*a)

