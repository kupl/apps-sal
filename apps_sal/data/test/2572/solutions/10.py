import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

#from math import ceil

def solve():
	n, m = mints()
	a = [None]*n
	for i in range(n):
		a[i] = list(mints())
	res = 0
	for i in range(n):
		if i <= n-1-i:
			for j in range(m):
				if j <= m-1-j:
					s = set([(x,y) for x in (i, n-1-i) for y in (j, m-1-j)])
					v = [a[x][y] for x, y in s]
					v.sort()
					c = v[len(v)//2]
					for x in v:
						res += abs(x-c)
	print(res)

for i in range(mint()):
	solve()

