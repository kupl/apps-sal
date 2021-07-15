(n, s) = [int(i) for i in input().split()]
xy = []
for i in range(n):
	xy.append(tuple(int(i) for i in input().split()))
ans = -1
for pair in xy:
	if (s > pair[0]) or (s == pair[0] and pair[1] == 0):
		ans = max(ans, (100 - pair[1]) % 100)
print(ans)
