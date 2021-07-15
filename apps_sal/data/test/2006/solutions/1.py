#!/usr/bin/env python3

def read_ints():
	return list(map(int, input().strip().split()))

n, m = read_ints()

best = 0
opts = set()

for _ in range(n):
	x = input()
	g = x.find('G')
	s = x.find('S')

	if s<g:
		best = float('inf')
		break
	else:
		opts.add(max(best, s-g))

if best == float('inf'):
	print(-1)
else:
	print(len(opts))


