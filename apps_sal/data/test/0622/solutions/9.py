n, k = [int(x) for x in input().strip().split(" ")]
le = 2**n - 1

def binsearch(level, le, ind):
	if level == 1:
		return 1
	if ind == le // 2 + 1:
		return level
	if ind > le // 2 + 1:
		ind -= le // 2 + 1
	return binsearch(level-1, le//2, ind)

print(binsearch(n,le,k))
