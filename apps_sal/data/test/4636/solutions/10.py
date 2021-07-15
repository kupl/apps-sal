import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n = mint()
	c = list(mints())
	l = 1
	r = n
	a = c[0]
	b = 0
	la = c[0]
	lb = 0
	ans = 1
	while l<r:
		x = 0
		ans += 1
		while x <= la and l < r:
			r -= 1
			x += c[r]
		lb = x
		b += x
		if l >= r:
			break
		ans += 1
		x = 0
		while x <= lb and l < r:
			x += c[l]
			l += 1
		la = x
		a += x
	print(ans, a, b)

for i in range(mint()):
	solve()

