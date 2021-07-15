n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# left = -1
# right = n-1

# while right - left > 1:
# 	mid = (right+left)//2
	
# 	count = 0
# 	curr = 0
# 	for i in range(mid, n):
# 		if curr + a[i] <= k:
# 			curr += a[i]
# 		else:
# 			count += 1
# 			curr = a[i]
# 	count += 1
	
# 	if count > m:
# 		left = mid
# 	else:
# 		right = mid

# print(n-right)

count = 0
curr = 0
i = n
while count < m and i >= 0:
	i -= 1
	if curr + a[i] <= k:
		curr += a[i]
	else:
		count += 1
		curr = a[i]

print(n-i-1)
