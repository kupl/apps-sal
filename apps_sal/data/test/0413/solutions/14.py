from math import ceil
n, m = list(map(int, input().split()))
step = 0
if n >= m:
	step += n-m
else:
	k = m
	while n < k:
		k = k / 2
	while n != m:
		if n - 1>= k:
			n -= 1
			step += 1
		else:
			k = 2*k
			n = 2*n
			step += 1
print(step)

