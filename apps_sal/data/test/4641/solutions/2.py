import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n,x = mints()
	c = [0]*x
	ans = 0
	for i in range(n):
		y = mint()
		c[y%x] += 1
		while c[ans%x] > 0:
			c[ans%x] -= 1
			ans += 1
		print(ans)

solve()


