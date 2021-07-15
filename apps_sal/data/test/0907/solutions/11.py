from itertools import combinations

n,m=list(map(int,input().split()))
c=[[] for i in range(n+1)]
p=[]
for i in range(m):
	x,y=list(map(int,input().split()))
	p.append([x,y])


x=p[0]
arr=[x[0],x[1]]
for i in p:
	if len(set(x).intersection(set(i)))==0:
		arr.append(i[0])
		arr.append(i[1])
		break

for i in range(m):
	for j in arr:
		if j in p[i]:
			c[j].append(i)


x=list(combinations(arr,2))
req=[i for i in range(m)]

for i in x:
	n1=i[0]
	n2=i[1]
	if list(set(c[n1]+c[n2]))==req:
		print("YES")
		return

print("NO")

