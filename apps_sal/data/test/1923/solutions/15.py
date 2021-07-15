n=int(input())
ans=int(0)

A=list(map(int,input().split()))

A.sort()
for i in range(n):
	ans+=A[i*2]
print(ans)


