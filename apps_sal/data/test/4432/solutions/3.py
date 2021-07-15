for i in range(int(input())):
	n=int(input())
	a=[int(j) for j in input().split()]
	s=0
	mx=a[0]
	for j in range(n):
		if(a[j]*mx<0):
			s+=mx
			mx=a[j]
		else:
			mx=max(mx, a[j])
	print(s+mx)
