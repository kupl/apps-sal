def resolve():
	n = int(input())
	x = list(map(int,input().split()))
	p = round(sum(x)/n)
	ans = 0
	for i in range(n):
		ans += (x[i]-p)**2
	print(ans)
resolve()
