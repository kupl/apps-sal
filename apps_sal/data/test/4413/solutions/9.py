

for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split(" ")))
	a=sorted(a)

	now=-1

	ans=1

	for i in a:
		if(abs(i-now)<=1):
			ans=2
			break
		now=i

	print(ans)
