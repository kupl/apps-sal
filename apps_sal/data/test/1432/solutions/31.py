N=int(input())
A=list(map(int,input().split()))
X=[]
s=sum(A)
for i in range(1,N,2):
  s-=2*A[i]
X.append(s)

for i in range(N-1):
  x=2*A[i]-X[i]
  X.append(x)
print((*X))

