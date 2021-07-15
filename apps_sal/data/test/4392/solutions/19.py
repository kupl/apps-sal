for _ in range(int(input())):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	pos=list(map(lambda x:int(x)-1,input().split()))
	z=sorted(list(l))
	d={}
	s=set(pos)
	sor={}
	flag="YES"
	for i in range(n):
		d[l[i]]=i
		sor[z[i]]=i
	for i in range(n):
		for j in range(min(d[l[i]],sor[l[i]]),max(d[l[i]],sor[l[i]])):
			if j not in s:
				flag="NO"
	print(flag)
