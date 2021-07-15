n=int(input())
arr=list(map(int,input().strip().split(' ')))
p=min(arr)
flag=0
ans=100000000
for i in range(n):
	if(arr[i]==p and flag==0):
		start=i
		flag=1
	elif(arr[i]==p and flag==1):
		ans=min(ans,i-start)
		start=i
print(ans)


