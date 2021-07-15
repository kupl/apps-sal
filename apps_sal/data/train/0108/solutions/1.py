for nt in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	point = -1
	for i in range(n):
		if l[i]<i:
			point = i-1
			break
	if point == -1:
		print ("Yes")
	else:
		flag=0
		for i in range(n-1,point-1,-1):
			if l[i]<(n-1-i):
				flag=1
				print ("No")
				break
		if flag==0:
			print ("Yes")
