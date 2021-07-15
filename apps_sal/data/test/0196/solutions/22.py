#!/usr/bin/env python3


mod = 10**9 + 7


[x, k] = list(map(int, input().strip().split()))

if x == 0:
	print(0)
	return


def pow2(n):
	if n == 0:
		return 1
	if n % 2 == 0:
		return (pow2(n // 2) ** 2) % mod
	else:
		return (((pow2(n // 2) ** 2) % mod) * 2) % mod

print((pow2(k) * ((2 * x - 1) % mod) + 1) % mod)

