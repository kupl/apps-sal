n,k=map(int,input().split());A=[1]+[0]*n;S=[[*map(int,input().split())]for _ in"_"*k];m=998244353
for i in range(1,n):
  A[i]+=A[i-1]
  for l,r in S:
    if i>r:A[i]-=A[i-r-1]
    if i>=l:A[i]+=A[i-l]
  A[i]%=m
print((A[n-1]-A[n-2])%m)
