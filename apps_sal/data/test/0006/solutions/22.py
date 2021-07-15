from bisect import bisect_left as bl
from collections import defaultdict as dd


for _ in range(int(input())):
	n, x = [int(i) for i in input().split()]
	l = []
	f = dd(int)
	for j in range(n):
		d, h = [int(i) for i in input().split()]
		l.append(d - h)
		f[d] = 1
	#print(n, x)
	l.sort(reverse = 1)
	#print(l)
	ans = 1
	x -= max(f.keys())
	if x <= 0:
		print(ans)
	else:
		if l[0] <= 0:
			ans = -1
		else:
			ans = x // l[0]
			if (x % l[0]) == 0:
				ans += 1
			else:
				ans += 2
		print(ans)
