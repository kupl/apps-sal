t = int(input())
for z in range(t):
	a,b = list(map(int,input().split()))
	ans = 0
	if a>b:
		if (a-b)%2 == 0:
			ans = 1
		else:
			ans = 2
	elif a<b:
		if (b-a)%2 == 0:
			ans = 2
		else:
			ans = 1
	print(ans)

