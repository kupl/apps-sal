from itertools import permutations
n,C=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(C)]
c=[list(map(int,input().split())) for _ in range(n)]
a=[[0]*C for _ in range(3)]
for i in range(n):
	for j in range(n):
		a[(i+j)%3][c[i][j]-1]+=1
ans=10**9
for v in permutations(range(C),3):
	tmp=0
	for i in range(3):
		for j in range(C):
			tmp+=a[i][j]*d[j][v[i]]
	ans=min(ans,tmp)
print(ans)
