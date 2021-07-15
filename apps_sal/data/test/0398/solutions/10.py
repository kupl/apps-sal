
def __starting_point():
	n, = map(int, input().split())
	a = list(map(int, input().split()))
	res = False
	a.sort()
	for i in range(1, n-1):
		if a[i-1] + a[i] > a[i+1]:
			res = True
			break
	if res:
		print("YES")
	else:
		print("NO")
__starting_point()
