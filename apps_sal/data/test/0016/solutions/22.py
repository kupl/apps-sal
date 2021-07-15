import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

a = [0]*4
for i in range(4):
	a[i] = mint()
if a[0]-a[3] != 0 or a[0] == 0 and a[2] > 0:
	print(0)
else:
	print(1)

