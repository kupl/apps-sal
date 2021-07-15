from sys import stdin

def solve(n, v, k):
	result = []
	for i in range(0, len(k)):
		if v > min(k[i]):
			result.append(i + 1)
	return result


def __starting_point():
	s = stdin.readline().split(' ')
	n = int(s[0])
	v = int(s[1])
	k = []
	for i in range(0, n):
		sn = stdin.readline().split(' ')[1:]
		ki = [int(kij) for kij in sn]
		k.append(ki)
	solution = solve(n, v, k)
	l = len(solution)
	print(l)
	if l > 0:
		print(' '.join([str(x) for x in solution]))

__starting_point()
