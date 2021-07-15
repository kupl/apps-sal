#!/usr/bin/env python3

import sys

[R, C] = list(map(int, sys.stdin.readline().strip().split()))
field = [sys.stdin.readline().strip() for _ in range(R)]

for line in field:
	if ('WS' in line) or ('SW' in line):
		print ('No')
		return
for l1, l2 in zip(field[1:], field[:-1]):
	for c1, c2 in zip(l1, l2):
		if (c1 == 'W' and c2 == 'S') or (c1 == 'S' and c2 == 'W'):
			print ('No')
			return

for i in range(R):
	field[i] = field[i].replace('.', 'D')

print ('Yes')
for line in field:
	print (line)

