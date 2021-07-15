def cmb(n,r):
  if n<0:
    return 0
  if n==0:
    if r!=0:
      return 0
    else:
      return 1
  elif r<0:
    return 0
  elif r>n:
    return 0
  elif r==0:
    return 1
  elif r==n:
    return 1
  else:
    return A[n]*B[r]*B[n-r]%mod
mod=998244353
A=[1,1]
B=[1,1]
for i in range(2,4005):
  A.append(A[-1]*i%mod)
  B.append(B[-1]*pow(i,mod-2,mod)%mod)
k,n=map(int,input().split())
if k==1:
  print(0)
  return
ans=[0]*(2*k+1)
for i in range(2,k+3):#i,i+1(i%2=0,i<k(くらい))で同じとか自明か？？？？？
  if i%2==0:
    i=i+1
    for j in range(min(n+1,i//2+1)):
      ans[i-1]=(ans[i-1]+cmb(n+k-i,k-i+j)*cmb(i//2,j)*pow(2,j,mod))%mod
  else:
    ans[i]=ans[i-1]
for i in range(k+2,2*k+1):
  ans[i]=ans[2*k+2-i]
for i in range(2,2*k+1):
  print(ans[i])
