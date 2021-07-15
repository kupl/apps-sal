n=int(input())
arr=list(map(int,input().split()))
dict1={}
ans=0
for i in range(n):
	for j in range(i+1,n):
		try:
			dict1[arr[i]+arr[j]]+=1
		except:
			KeyError
			dict1[arr[i]+arr[j]]=1
		ans=max(ans,dict1[arr[i]+arr[j]])
print(ans)


