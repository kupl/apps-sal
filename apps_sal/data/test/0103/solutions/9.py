n = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
	for j in range(i + 2, n):
		if arr[j] - arr[i] == j - i:
			ans = max(ans, j - i - 1)
for i in range(n):
	if arr[i] == i + 1:
		ans = max(ans, i)
for i in range(n):
	if n - i - 1 == 1000 - arr[i]:
		ans = max(ans, n - i - 1)
print(ans)
