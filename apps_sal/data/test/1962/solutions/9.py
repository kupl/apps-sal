#!/usr/bin/env python3

from bisect import bisect

[n, k, l] = list(map(int, input().strip().split()))
ais = list(map(int, input().strip().split()))

ais.sort()
if ais[n - 1] - ais[0] > l:
	print(0)
	return

inds = list(range(0, n * k, k))
bnd = bisect(ais, ais[0] + l) - 1
for i in range(1, n):
	inds[i] = min(inds[i], bnd)

for i in range(n - 1, 1, -1):
	if inds[i] <= inds[i - 1]:
		inds[i - 1] = inds[i] - 1

print(sum(ais[i] for i in inds))

