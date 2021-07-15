def maxx(n):
	return n&-n
n,q=map(int,input().split())
root=n//2+1
while q>0:
	x=int(input())
	s=input()

	for i in s:
		if i=='U' and x!=root:
			p=x+maxx(x)
			if x==p-maxx(p)//2:
				x=p
			else:
				x=x-maxx(x)
		elif i=='L':
			x=x-maxx(x)//2
		elif i=='R':
			x=x+maxx(x)//2
	q=q-1
	print(x)
