n,d=map(int,input().split())
t=[]
for i in range(n):
	x,y=map(int,input().split())
	t+=[(x,y)]
t=sorted(t, key=lambda colonnes: colonnes[0])
i=0
j=1
(q,r)=t[0]
vTemp=r
rTemp=r
qtemp=q
v=vTemp
while j<n:
	(x,y)=t[j]
	if x>=q+d:
		vTemp-=rTemp
		i+=1
		(q,r)=t[i]
		qTemp=q
		rTemp=r
	else:
		vTemp+=y
		v=max(v,vTemp)
		j+=1
print(v)
