import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int, minp().split()))

def solve():
	n = mint()
	x = list(mints())
	x.sort()
	r = 0
	w = [0]*(n+2)
	c = [0]*(n+2)
	for i in x:
		c[i] += 1
		if w[i-1] == 0:
			w[i-1] += 1
			r += 1
		elif w[i] == 0:
			w[i] += 1
			r += 1
		elif w[i+1] == 0:
			w[i+1] += 1
			r += 1

	rm = r
	r = 0
	w = [0]*(n+2)
	for i in range(1,n+1):
		v = c[i]
		if v != 0:
			if w[i+1] > 0:
				pass
			elif w[i] > 0:
				pass
			elif w[i-1] > 0:
				pass
			else:
				w[i+1] += v
				r += 1
	print(r,rm)

#for i in range(mint()):
solve()

