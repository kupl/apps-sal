n,k=map(int,input().split())
arr=list(map(int,input().split()))
find=[0]*n
for i in range(n):
	find[i]=[0]*n
presum=[0]*n
presum[0]=arr[0]
for i in range(1,n):
	presum[i]=presum[i-1]+arr[i]
for i in range(n-k+1):
	for j in range(i+k-1,n):
		if i==0:
			find[i][j]=presum[j]/(j+1)
		else:
			find[i][j]=(presum[j]-presum[i-1])/(j-i+1)
maxi=0
for i in range(n):
	for j in range(n):
		if find[i][j]>maxi:
			maxi=find[i][j]
print(maxi)
