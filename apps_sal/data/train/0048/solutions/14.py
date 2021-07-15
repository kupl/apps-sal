import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	x, y, k = mints()
	ta = k*(y+1)
	d = ((ta-1)+(x-2))//(x-1)
	print(d+k)

for i in range(mint()):
	solve()

