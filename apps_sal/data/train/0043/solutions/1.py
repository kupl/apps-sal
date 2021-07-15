def helper(m):
	s = 0
	for i in range(len(a)):
		if a[i] > m:
			s += b[i]
	return s <= m

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	l, r = 1, 10**9

	while l < r:
		mid = l + (r-l)//2
		temp = helper(mid)

		if temp:
			r = mid
		else:
			l = mid+1
	print(l)



