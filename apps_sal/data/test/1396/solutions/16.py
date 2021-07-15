from itertools import groupby

def destroy(chain):
	remaining = []
	for k, v in groupby(chain):
		L = list(v)
		if len(L) < 3:
			remaining.extend(L)
	if len(chain) == len(remaining):
		return len(remaining)
	else:
		return destroy(remaining)

def solve():
	n, k, x = list(map(int, input().split()))
	balls = list(map(int, input().split()))
	res = 0
	for i in range(n):
		tmp = balls[:]
		tmp.insert(i, x)
		res = max(res, n-destroy(tmp))
	return res

def __starting_point():
	print(solve())

__starting_point()
