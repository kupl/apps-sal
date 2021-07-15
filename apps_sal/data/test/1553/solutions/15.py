n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
l, r = 1, n + 1
while l + 1 < r:
	mid = (l + r) >> 1
	c = sorted(a[:mid], reverse=True)
	if sum(c[i] for i in range(len(c)) if (i & 1) == 0) <= h:
		l = mid
	else:
		r = mid
print(l)

