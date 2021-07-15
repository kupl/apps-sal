h,w=map(int,input().split())
arr=[]
for i in range(h):
	s=str(input())
	arr1=[]
	for j in range(w):
		arr1.append(s[j])
	arr.append(arr1)
flag=0
h1=-1
w1=-1
for i in range(1,h-1):
	for j in range(1,w-1):
		if(arr[i][j]=='*'):
			if(arr[i-1][j]==arr[i+1][j]==arr[i][j-1]==arr[i][j+1]=='*'):
				flag=1
				h1=i
				w1=j
				break
	if(flag==1):
		break
if(flag==1):
	i=h1
	while(i>=0 and arr[i][w1]=='*'):
		arr[i][w1]='?'
		i-=1

	i=h1+1
	while(i<h and arr[i][w1]=='*'):
		arr[i][w1]='?'
		i+=1

	j=w1-1
	while(j>=0 and arr[h1][j]=='*'):
		arr[h1][j]='?'
		j-=1
	j=w1+1
	while(j<w and arr[h1][j]=='*'):
		arr[h1][j]='?'
		j+=1

	# for i in range(h):
	# 	print(*arr[i])

	flag2=0
	for i in range(h):
		for j in range(w):
			if(arr[i][j]=='*'):
				flag2=1
				break
		if(flag2==1):
			break

	if(flag2==0):
		print('YES')
	else:
		print('NO')
else:
	print('NO')
