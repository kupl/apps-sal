for nt in range(int(input())):
	n,m=map(int,input().split())
	if n==1:
		print (0)
		continue
	if n==2:
		print (m)
		continue
	print (2*m)
