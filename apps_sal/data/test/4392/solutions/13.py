for nt in range(int(input())):
	n,m=list(map(int,input().split()))
	arr=list(map(int,input().split()))
	p=list(map(int,input().split()))
	if m>=n-1:
		print ("YES")
		continue
	flag=0
	for i in range(n): 
		for j in range(0, n-i-1): 
			if arr[j] > arr[j+1] :
				if (j+1) not in p:
					flag=1
					break
				arr[j], arr[j+1] = arr[j+1], arr[j] 
	if flag==1:
		print ("NO")
	else:
		print ("YES")

