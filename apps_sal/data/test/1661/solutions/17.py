n,m=list(map(int,input().strip().split()))
ci=list(map(int,input().strip().split()))
ai=list(map(int,input().strip().split()))
i=0
j=0
count=0
while(i<n and j<m):
	if ci[i]<=ai[j]:
		i=i+1
		j=j+1
		count=count+1
	else:
		i=i+1
print (count)


