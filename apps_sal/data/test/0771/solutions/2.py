n,k,m=map(int,input().split())
a=list(map(int,input().split()))

b=[0]*m
for x in a:
	b[x%m]+=1

for i in range(m):
	if b[i]>=k:
		print('Yes')
		cnt=k
		for x in a:
			if cnt==0:
				break
			if x%m==i:
				print(x,end=' ')
				cnt-=1

		return
	
print('No')

