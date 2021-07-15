N,K=list(map(int,input().split()))
mod=998244353
L=[0]*K;R=[0]*K
m=[0]*3*N
m[0]=1;m[1]=-1
for i in range(K):
  L[i],R[i]=list(map(int,input().split()))

for j in range(N):
  m[j+1]+=m[j]%mod
  for i in range(K):
    if j+L[i]>N-1:continue
    m[j+L[i]] +=m[j]%mod
    m[j+R[i]+1] -=m[j]%mod
print((m[N-1]%mod))

