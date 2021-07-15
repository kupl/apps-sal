n = int(input())
arr = list(map(int, input().split()))
ans = 0
res = None
for i in range(n):
	temp = list(arr)
	mini = arr[i]
	for j in range(i-1, -1, -1):
		temp[j] = min(temp[j], mini)
		mini = min(mini, temp[j])
	mini = arr[i]
	for j in range(i+1, n):
		temp[j] = min(temp[j], mini)
		mini = min(mini, temp[j])
	s = sum(temp)
	if s > ans:
		ans = s
		res = list(temp)
print(*res)
