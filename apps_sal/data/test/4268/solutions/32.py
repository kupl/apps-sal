import itertools

N,D=map(int, input().split())
X=[list(map(int, input().split())) for _ in range(N)]

combi=list(itertools.combinations([i for i in range(N)],2 ))

ans=0

for c in combi:
	temp=0
	for d in range(D):
		temp+=(X[c[0]][d]-X[c[1]][d])**2
	temp=temp**.5
	if float.is_integer(temp):ans+=1

print(ans)
