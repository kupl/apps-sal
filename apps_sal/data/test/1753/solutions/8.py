import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n, m = mints()
a = []
p = [None]*n
for i in range(n):
	p[i] = []
for i in range(m):
	x, y = mints()
	p[x-1].append((i+1,x))
	p[y-1].append((i+1,y))
for i in range(n):
	p[i].append((m+1+i,i+1))
for i in range(n):
	print(len(p[i]))
	for j in p[i]:
		print(*j)
