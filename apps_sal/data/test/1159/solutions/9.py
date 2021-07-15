prime=[True]*1501
prime[0]=False
prime[1]=False
for i in range(2,1501):
	if prime[i]:
		for j in range(i*i,1501,i):
			prime[j]=False
n=int(input())
degree=[2]*n
ans=[]
edges=n
for i in range(n-1):
	ans.append([i+1,i+2])
ans.append([1,n])
c=0
while(not prime[edges]):
	ans.append([c+1,c+n//2+1])
	#print(edges,c,c+n//2)
	degree[c]+=1
	degree[c+n//2]+=1
	c+=1
	edges+=1
print(len(ans))
for i in ans:
	print(i[0],i[1])

