TIME_IN_A_DAY = 86400
n, t = map(int, input().split())
a = list(map(int, input().split()))
for i in range(len(a)):
	if TIME_IN_A_DAY - a[i] >= t:
		print(i + 1)
		break
	t -= (TIME_IN_A_DAY - a[i])
