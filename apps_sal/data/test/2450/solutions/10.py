t = int(input())
for _ in range(t):
	n, m, x, y = map(int, input().split())
	ans = 0
	if y > 2*x:
		y = 2*x

	for i in range(n):
		arr = input()

		i = 0
		while i < m:
			if arr[i] == "*":
				i += 1
			else:
				if i + 1 < m and  arr[i+1] == ".":
					ans += y
					i += 2
				else:
					ans += x
					i += 1

	print(ans)
