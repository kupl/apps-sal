for _ in range(int(input())):
	n = int(input())
	if n == 4:
		print(3, 1, 4, 2)
		continue
	if n < 5:
		print(-1)
		continue
	arr = []
	done = [False] * n
	for i in range(0, n, 2):
		arr.append(i)
		done[i] = True
	for i in range(arr[-1]-3, 0, -4):
		arr.append(i)
		done[i] = True
	for i in range(n):
		if not done[i]:
			arr.append(i)

	print(*[e+1 for e in arr])

