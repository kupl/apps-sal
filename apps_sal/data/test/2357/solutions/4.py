t = int(input())
for i in range(t):
	n = int(input())
	mas = list(map(int, input().split()))
	ans = []
	mini = n
	for i in range(n):
		ans.append([mas[i], i])
	ans.sort()
	flag = False
	for i in range(n - 1):
		if ans[i][0] == ans[i + 1][0]:
			mini = min(ans[i + 1][1] - ans[i][1] + 1, mini)
			flag = True
	if not(flag):
		print(-1)
	else:
		print (mini)

