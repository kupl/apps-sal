for t in range(int(input())):
	s = input()
	last = -1
	num = []
	n = len(s)
	for i in range(n):
		if (s[i] == "0"):
			if (i - last - 1 > 0):
				num.append(i - last - 1)
			last = i
	if (n - last - 1 > 0):
		num.append(n - last - 1)
	num = sorted(num)[::-1]
	ans = 0
	for i in range(0, len(num), 2):
		ans += num[i]
	print(ans)
