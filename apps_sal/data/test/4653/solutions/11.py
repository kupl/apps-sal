import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n, k = mints()
	x = n // k
	r = n % k
	if r > k // 2:
		print(n - (r - k//2))
	else:
		print(n)

for i in range(mint()):
	solve()

