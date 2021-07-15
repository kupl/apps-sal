#!/usr/bin/env python3

import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())
xys = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

xys = list(set(xys))
if len(xys) < 5:
	print ('YES')
	return

def is_on_line(p0, p1, p2):
	return ((p1[0] - p0[0]) * (p2[1] - p0[1]) == (p1[1] - p0[1]) * (p2[0] - p0[0]))

l1 = (-1, -1, -1)
for comb in combinations(list(range(5)), 3):
	if is_on_line(xys[comb[0]], xys[comb[1]], xys[comb[2]]):
		l1 = comb
		break

if l1[0] < 0:
	print ('NO')
	return

line = [0 for _ in range(n)]
for l in l1:
	line[l] = 1

for i in range(n):
	if i in l1:
		continue
	if is_on_line(xys[l1[0]], xys[l1[1]], xys[i]):
		line[i] = 1

nline = [i for i in range(n) if line[i] == 0]
if len(nline) < 3:
	print ('YES')
	return

for i in nline[2:]:
	if not is_on_line(xys[nline[0]], xys[nline[1]], xys[i]):
		print ('NO')
		return

print ('YES')

