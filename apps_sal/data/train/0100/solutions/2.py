for _ in range(int(input())):
	l = sorted(map(int, input().split()))
	print(min(sum(l) // 2, l[0] + l[1]))
