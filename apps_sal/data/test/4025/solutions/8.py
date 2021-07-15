a, b, c = list(map(int, input().split()))

a_week = a // 3
b_week = b // 2
c_week = c // 2

week = min(a_week, b_week, c_week)

a -= week * 3
b -= week * 2
c -= week * 2

# Do simulation
max_day = 0

for i in range(7):

	aa = a
	bb = b
	cc = c
	count = 0

	for j in range(7):

		day = (i + j) % 7

		if day == 0 or day == 3 or day == 6:
			aa -= 1
		elif day == 1 or day == 5:
			bb -= 1
		else:
			cc -= 1

		if aa < 0 or bb < 0 or cc < 0:
			break
		count += 1

	if count > max_day:
		max_day = count

result = week * 7 + max_day
print(result)

