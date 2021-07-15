def bp(n, t):
	l = 0
	r = n
	while r - l > 1:
		m = l + (r - l) // 2
		if x[m] <= t:
			l = m
		else:
			r = m
	if x[l] > t:
		l = -1
	return l + 1

n = int(input())
x = [int(i) for i in input().split()]
x.sort()
q = int(input())
for k in range(q):
	tmp = int(input())
	print(bp(n, tmp))
	

