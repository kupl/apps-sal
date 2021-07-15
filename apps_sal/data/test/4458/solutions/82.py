N=int(input())
P=list(map(int, input().split()))

ans=0
tempmin=P[0]

for i in range(N):
	if tempmin>=P[i]:
		#print(tempmin,P[i])
		ans+=1
	tempmin=min(tempmin,P[i])
	
print(ans)
