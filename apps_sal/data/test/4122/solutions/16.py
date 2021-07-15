H,n=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr1=[]
mostmin=10**9
val=0
mostminindex=-1
for i in range(n):
	val+=arr[i]
	arr1.append(val)
	if(mostmin>val):
		mostmin=val
		mostminindex=i
if(mostmin>=0):
	print(-1)
elif(abs(mostmin)<H and val>=0):
	print(-1)
else:
	turns=-1
	if(H+mostmin<=0):
		turns=0
	else:
		if(val!=0):
			turns=(H-abs(mostmin))//abs(val)
		else:
			turns=0
		#print(turns)
	H-=(abs(val)*turns)
	minutes=n*turns
	for i in range(n):
		if(H+arr1[i]<=0):
			print(minutes+1)
			return
		else:
			minutes+=1
	H-=abs(val)
	for i in range(n):
		if(arr1[i]+H<=0):
			print(minutes+1)
			return
		else:
			minutes+=1
	print(-1)


