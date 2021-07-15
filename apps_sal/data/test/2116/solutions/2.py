n,m,k=list(map(int,input().split()))
p=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(n)]
st=0
for i in range(n):
	for j in range(m):
		for g in range(k):
			if a[i][j]==p[g]:
				p.insert(0,p[g])
				del(p[g+1])
				st+=g+1
				g-=1		
print(st)

