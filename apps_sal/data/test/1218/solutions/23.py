n, k = list(map(int, input().split()))
l, r = -1, k+1
while l+1 < r:
	mid = l + r >> 1
	val = (k - mid + 1 + k) * mid // 2 - (mid - 1)
	if val < n:
		l = mid
	else:
		r = mid
print(-1 if r == k+1 else r)

