n = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
	print(arr[i], arr[-1-i])
