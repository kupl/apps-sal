#!/bin/python3

a, b = list(map(int, input().split()))

maxval = min(b - 1, a)
minval = b - maxval


d = maxval - minval + 1
if d < 0:
	d = 0

erg = d // 2
print(erg)

