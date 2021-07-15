n,k=list(map(int,input().strip().split()))
l=list(map(int,input().strip().split()))
i=0
j=1
l.sort()
le=len(l)
deletion=0
valid=[0 for i in range(le)]
while(j<le and i<le):
	if (valid[i]==1):
		i=i+1
		continue
	elif (i==j):
		j=j+1
		continue
	elif (l[i]<l[j] and l[j]<=(l[i]+k)):
		deletion=deletion+1
		valid[i]=1
		i=i+1
	elif (l[i]==l[j]):
		j=j+1
		continue
	else:
		i=i+1
print(le-deletion)

