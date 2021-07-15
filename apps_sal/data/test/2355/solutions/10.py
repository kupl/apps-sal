t = int(input())
while(t > 0):
	n, p = list(map(int, input().split()))
	temp = 2 * n + p
	l = 1
	r = l + 1
	while(temp > 0):
		if(r == n + 1):
			l += 1
			r = l + 1
		print(l,r)
		r += 1
		temp -= 1
	t -= 1

