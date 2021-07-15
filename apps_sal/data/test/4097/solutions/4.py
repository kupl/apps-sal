def cal(x, y):
	d = a[1] + y - a[0] - x
	wk1 = a[1] + y
	wkans = 0
	for k in range(2,n):
		diff = abs((wk1 + d) - a[k])
		if diff == 1:
			wkans += 1
		elif diff > 1:
			return n + 1
		wk1 += d
	return wkans
			

n = int(input())
a = [int(i) for i in input().split()]

if n > 2:
	ans_final = n + 1
	for i in range(-1, 2):
		for j in range(-1, 2):
			ans_final = min(ans_final, cal(i, j) + abs(i) + abs(j))
else:
	ans_final = 0
if ans_final == n + 1:
	print(-1)
else:
	print(ans_final)

