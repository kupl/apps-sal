n,r = map(int, input().split())
list_a = list(map(int, input().split()))
#first
count = 0
next = 0
i = 0
ans = 0
if n <= r:
	if 1 in list_a:
		count = 1
	else:
		ans = -1
else:
	while True:
		if i > r-1:
			ans = -1
			break
		elif list_a[r-1-i] == 1:
			next = r-1-i
			count += 1
			break
		else:
			i += 1
	flag = 0
	if ans != -1:
		while True:
			i = 0
			while True:
				if i >= 2*(r-1) + 1:
					ans = -1
					break
				try:
					if list_a[next + 2*(r-1) + 1 - i] == 1:
						next += 2*(r-1) + 1 - i
						count += 1
						break
					else:
						i += 1
				except IndexError:
					flag = 1
					break
			if ans == -1 or flag == 1:
				break
	if ans != -1:
		if next >= n-r:
			pass
		else:
			while True:
				if i > r-1:
					ans = -1
					break
				elif list_a[-r + i] == 1:
					count += 1
					break
				else:
					i += 1
if ans == -1:
	print(ans)
else:
	print(count)
