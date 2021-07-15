n,m=list(map(int,input().split()))
arr1=[]
for i in range(n):
	temp=list(map(int,input().split()))
	arr1.append(temp)
arr2=[]
for i in range(n):
	temp=list(map(int,input().split()))
	arr2.append(temp)

flag=0
for i in range(n):
	temparr1=[]
	temparr2=[]
	indexi=i
	indexj=0
	while(indexi>=0 and indexj<m):
		temparr1.append(arr1[indexi][indexj])
		temparr2.append(arr2[indexi][indexj])
		indexi-=1
		indexj+=1
	temparr1.sort()
	temparr2.sort()
	#print(*temparr1)
	#print(*temparr2)
	for j in range(len(temparr1)):
		if(temparr1[j]!=temparr2[j]):
			flag=1
			break
if(flag==1):
	print('NO')
else:
	for i in range(1,m):
		temparr1=[]
		temparr2=[]
		indexi=n-1
		indexj=i
		while(indexi>=0 and indexj<m):
			temparr1.append(arr1[indexi][indexj])
			temparr2.append(arr2[indexi][indexj])
			indexi-=1
			indexj+=1
		temparr1.sort()
		temparr2.sort()
		#print(*temparr1)
		for j in range(len(temparr1)):
			if(temparr1[j]!=temparr2[j]):
				flag=1
				break
	if(flag==0):
		print('YES')
	else:
		print('NO')

