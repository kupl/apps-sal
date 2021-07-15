for nt in range(int(input())):
	a,b=map(int,input().split())
	if b==a:
		print (0)
		continue
	if b>a:
		if (b-a)%2==1:
			print (1)
			continue
		else:
			print (2)
			continue
	else:
		if (a-b)%2==0:
			print (1)
			continue
		else:
			print (2)
