for nt in range(int(input())):
	x,y,n = map(int,input().split())
	r = n%x
	if r==y:
		print (n)
		continue
	if y<r:
		print (n-(r-y))
		continue
	print (n-(x)+(y-r))
