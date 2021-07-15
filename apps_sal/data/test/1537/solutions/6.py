n,k=map(int,input().split())
s=[]
for i in range(n):
	s+=[input()]
y=[[n,0] for i in range(n)]
z=[[n,0] for i in range(n)]
r=0
for i in range(n):
	ind1=n
	ind2=-1
	for j in range(n):
		if s[i][j]=='B':
			ind1=min(j,ind1)
			ind2=max(j,ind2)
	if ind1!=n:
		y[i]=[max(0,ind2+1-k),ind1]
	else:
		r+=1
for j in range(n):
	ind1=n
	ind2=-1
	for i in range(n):
		if s[i][j]=='B':
			ind1=min(i,ind1)
			ind2=max(i,ind2)
	if ind1!=n:
		z[j]=[max(0,ind2+1-k),ind1]
	else:
		r+=1
x=[[0 for i in range(n)] for i in range(n+1)]
x2=[[0 for i in range(n+1)] for i in range(n)]
for a in range(n):
	for b in range(n):
		i=n-1-a
		j=n-1-b
		x[i][j]+=x[i+1][j]
		if y[i][0]<=j<=y[i][1]:
			x[i][j]+=1
		if i+k<=n-1 and y[i+k][0]<=j<=y[i+k][1]:
			x[i][j]-=1
for b in range(n):
	for a in range(n):
		i=n-1-a
		j=n-1-b
		x2[i][j]+=x2[i][j+1]
		if z[j][0]<=i<=z[j][1]:
			x2[i][j]+=1
		if j+k<=n-1 and z[j+k][0]<=i<=z[j+k][1]:
			x2[i][j]-=1
m=0
for i in range(n):
	for j in range(n):
		c=x[i][j]+x2[i][j]
		if c>m:
			m=c
print(m+r)
