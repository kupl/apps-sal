q = int(input())
for re in range(q):
	n, x, a, b = map(int,input().split())
	if abs(a-b) + x >= n - 1:
		print (n - 1)
	else:
		print(abs(a-b) + x)
