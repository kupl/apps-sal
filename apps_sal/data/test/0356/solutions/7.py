n=int(input())
alist=list(map(int,input().split()))
m=int(input())
blist=list(map(int,input().split()))

prea = [alist[0]]
for i in range(1,n):
	prea.append(prea[-1]+alist[i])

preb = [blist[0]]
for i in range(1,m):
	preb.append(preb[-1]+blist[i])
#print(prea,preb)
if prea[-1]!=preb[-1]:
	print(-1)

else:
	x=0
	y=0
	count=0
	while x<n and y<m:

		if prea[x]==preb[y]:

			count+=1
			x+=1
			y+=1
		elif prea[x]<preb[y]:
			x+=1
		else:
			y+=1

	print(count)



