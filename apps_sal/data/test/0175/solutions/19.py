#!/usr/bin/env python3

import sys

[a, b] = list(map(int, sys.stdin.readline().strip().split()))

while a != 0 and b != 0:
	a_old, b_old = a, b
	a %= 2 * b
	if a == 0:
		break
	b %= 2 * a
	if a == a_old and b == b_old:
		break

print(a, b)

