import sys

def minp():
	return sys.stdin.readline().strip()

def mint():
	return int(minp())

def mints():
	return list(map(int,minp().split()))

def solve():
	n = mint()
	s = set()
	w = set()
	k = 0
	r = []
	for i in mints():
		k += 1
		if i < 0:
			if (-i) not in s:
				print(-1)
				return
			s.remove(-i)
			if len(s) == 0:
				r.append(k)
				k = 0
				w = set()
		else:
			if i in w:
				print(-1)
				return
			s.add(i)
			w.add(i)
	if len(s) != 0:
		print(-1)
		return
	print(len(r))
	print(' '.join(map(str,r)))

solve()

