[n, m] = [int(i) for i in input().split()]
if m == n:
	print (0)
elif m == 0:
	print (1)
elif m * 2 <= n:
	print(m)
else:
	print(n - m)
