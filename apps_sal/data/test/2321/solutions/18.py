for t in range(int(input())):
	n = int(input())
	wo = input().strip()
	ii, jj = 0, 0
	i, j = 0, n-1
	while i < n and wo[i] == '<':
		ii += 1
		i += 1
	while j >= 0 and wo[j] == '>':
		j-=1
		jj += 1
	print(min(ii, jj))

