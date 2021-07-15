n, k = list(map(int, input().split()))
if k == 1 or n == 1:
	print(0)
	return
if k > 2 * n - 1:
	print(0)
else:
	left, right = 0, min(n - 1, k - 1)
	while left != right - 1:
		mid = (left + right) // 2
		if k - mid <= n:
			right = mid
		else:
			left = mid
	print(max(0, (min(n, k - 1) - right + 1)) // 2)

