from math import factorial

def C(n, k):
	return n - k + 1


n = int(input())
if n != 3:
    print(4 * (C(2 * n - 2, n) - 2) * 3 * 3 * 4 ** (n - 4) + 4 * 2 * 3 * 4 ** (n - 3))
else:
	print(24)

