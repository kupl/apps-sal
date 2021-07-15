import sys
from math import *

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return map(int, minp().split())

n = mint()
a = list(mints())
a.sort()
s = sum(a)
m = mint()
for i in mints():
	print(s - a[-i])
