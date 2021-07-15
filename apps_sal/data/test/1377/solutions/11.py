n = int(input())
a = list(map(int, input().split()))
idx = a.index(max(a))
for i in range(idx, 0, -1):
	if a[i] < a[i - 1]:
		print('NO')
		return
for i in range(idx, n - 1):
	if a[i] < a[i + 1]:
		print('NO')
		return
print('YES')
