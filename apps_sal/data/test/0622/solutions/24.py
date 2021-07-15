import math

n, k = list(map(int, input().split()))
arr = reversed([int(math.pow(2, i)) for i in range(50)])

for index, num in enumerate(arr):
	if k % num == 0:
		print(50 - index)
		break
