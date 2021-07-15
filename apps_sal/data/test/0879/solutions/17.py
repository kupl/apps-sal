def __starting_point():
	n = int(input())
	P = list(map(int, input().rstrip().split()))

	path = [n]
	while n != 1:
		n = P[n - 2]
		path.append(n)
	path.reverse()
	print(' '.join(map(str, path)))
__starting_point()
