for _ in range(int(input())):
	n = int(input())

	ans = {0}

	for i in range(1, int(n ** 0.5 + 1)):
		ans.add(n // i)
		ans.add(n // (n // i))

	print(len(ans))
	print(*sorted(ans))
