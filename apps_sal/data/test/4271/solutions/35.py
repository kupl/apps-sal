N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))

ans=0

for i in range(N-1):
	now=A[i]
	next=A[i+1]
	ans+=B[now-1]
	if next==now+1:
		ans+=C[now-1]

ans+=B[A[N-1]-1]

print(ans)
