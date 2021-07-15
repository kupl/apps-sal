import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

def deltas(a):
	r = [0]*(len(a)-1)
	for i in range(0,len(a)-1):
		r[i] = a[i+1]-a[i]
	r.sort()
	return r

n = mint()
a = list(mints())
b = list(mints())
print("Yes") if deltas(a) == deltas(b) and a[0] == b[0] else print("No")

