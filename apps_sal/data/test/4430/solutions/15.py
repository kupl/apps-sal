n,m,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr1=[0]*n
i=n-1
prevval=0
ans=0
while(i>=0 and m>0):
	if(prevval+arr[i]<=k):
		prevval+=arr[i]
	else:
		m-=1
		prevval=arr[i]
	i-=1
	ans+=1
if(m==0):
	ans-=1
print(ans)

