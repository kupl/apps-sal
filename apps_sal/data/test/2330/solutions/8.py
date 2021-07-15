for _ in range(int(input())):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	if m<n or n==2:
		print("-1")
		continue
	L=[[l[i],i+1]for i in range(n)]
	L.sort()
	ans1=2*sum(l)
	ans1+=(L[0][0]+L[1][0])*(m-n)
	print(ans1)
	for i in range(n-1):
		print(i+1,i+2)
	print(1,n)
	for i in range(m-n):
		print(L[0][1],L[1][1])
