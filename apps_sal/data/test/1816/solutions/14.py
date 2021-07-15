n=int(input())
ls=list(map(int,input().split()))
arr=[0]*n
for x in range(n):
	arr[ls[x]-1]=x
su=0
for x in range(1,n):
	su+=abs(arr[x]-arr[x-1])
print(su)
