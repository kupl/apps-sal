import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, K = list(map(int, input().split()))
A = np.array(list(map(int, input().split())), dtype = np.int64)
F = np.array(list(map(int, input().split())), dtype = np.int64)
A.sort()
F.sort()
F = F[::-1]

l = 0
r = 10**12 + 100

def solve(num):
	B = num // F
	tmp = np.sum(np.maximum(0, A - B))
	if tmp <= K:
		return 1
	else:
		return 0

while r - l > 1:
	mid = (l + r) // 2
	if solve(mid):
		r = mid
	else:
		l = mid

if solve(l):
	print(l)
else:
	print(r)


