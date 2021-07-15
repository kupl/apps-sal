n, m, k = [int(x) for x in input().split()]
if (k == -1) and ((n+m) % 2 == 1):
	print(0)
else:
	print(pow(2, (n-1)*(m-1), 1000000007))
