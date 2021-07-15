N=int(input())
W=list(map(int, input().split()))

ans=sum(W)
for t in range(N-1):
	#print(W[:t+1],W[t+1:])
	ans=min(abs(sum(W[:t+1])-sum(W[t+1:])),ans)

print(ans)
