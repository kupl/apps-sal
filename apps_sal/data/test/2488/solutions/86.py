n,d,a=map(int,input().split())
d=d*2
M=sorted([list(map(int,input().split())) for i in range(n)])
l=0
A=[0]*n
B=[0]
ans=0
for i in range(n):
  while M[l][0]+d<M[i][0]:
    l=l+1
  ans=ans+max(0,(M[i][1]-B[i]+B[l]+a-1)//a)
  A[i]=max(0,(M[i][1]-B[i]+B[l]+a-1)//a)*a
  B.append(B[-1]+A[i])
print(ans)
