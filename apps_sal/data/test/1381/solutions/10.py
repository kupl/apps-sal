#!/usr/bin/env python3

[k, n, s, p] = list(map(int, input().strip().split()))

def ceil(a, b):
	return -((-a) // b)

print(ceil(k * ceil(n, s), p))

