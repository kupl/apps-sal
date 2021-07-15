#!/usr/bin/env python3

from collections import deque

n = int(input().strip())
wis = list(map(int, input().strip().split()))
cs = input().strip()

pl = list(range(1, n + 1))
pl.sort(key=lambda p: wis[p - 1])

i = 0
stack = deque()
res = []
for c in cs:
	if c == '0':
		stack.append(pl[i])
		res.append(pl[i])
		i += 1
	else:
		res.append(stack.pop())

print(' '.join(map(str, res)))

