n=int(input())
A=list(map(int,input().split()))
b=sum(A)
for i in range(n-1):
	if A[i+1]<A[i]:
		A[i+1]=A[i]
print(sum(A)-b)
