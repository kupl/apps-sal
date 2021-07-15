f=lambda:map(int,input().split())
N,X=f()
*A,=f()
A=[0]+A

c=0
for i in range(N):
 c+=max(0,A[i]+A[i+1]-X)
 A[i+1]=min(A[i+1],X-A[i])
print(c)
