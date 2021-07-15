n=int(input())
d=[]
for i in range(n):
	d+=[[int(i) for i in input()]]
inf=200
for i in range(n):
	for j in range(n):
		if d[i][j]==0 and i!=j:
			d[i][j]=inf
for k in range(n):
	for j in range(n):
		for i in range(n):
			d[i][j]=min(d[i][j],d[i][k]+d[k][j])
m=int(input())
p=list(map(int,input().split()))
path=[p[0]]
j=0
k=0
i=0
while i<=m-1:
	if d[p[j]-1][p[i]-1]==i-j:
		k=i
		i+=1
	elif j!=k:
		path.append(p[k])
		j=k
		i-=1
path.append(p[m-1])
print(len(path))
print(" ".join(map(str,path)))	
