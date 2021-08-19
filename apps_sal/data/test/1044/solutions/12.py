"""
a = [0] * 3000

def mex(l):
	for i in range(3000):
		if i not in l:
			return i
	return 3000

a[1] = 0
for i in range(2, 3000):
	a[i] = mex([a[x] ^ a[i - x] for x in range(1, i)])
"""
from itertools import accumulate
n = int(input())
a = list(map(int, input().split(' ')))
b = list(accumulate((~a[i] & 1 for i in range(n)), lambda i, j: i ^ j))
for i in b:
    print('2' if i == 0 else '1')
