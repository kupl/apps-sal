n, m = map(int, input().split())
if m == 0:
	print(n, n)
	return
left, right = 0, n + 1
while left != right - 1:
	mid = (left + right) // 2
	if mid * (mid - 1) // 2 < m:
		left = mid
	else:
		right = mid
print(max(0, n - 2 * m), n - right)
