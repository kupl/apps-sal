n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
	for j in range(n - 1):
		if (arr[j] > arr[j + 1]):
			arr[j], arr[j+1] = arr[j+1], arr[j]
			print(j + 1, j + 1 + 1)
