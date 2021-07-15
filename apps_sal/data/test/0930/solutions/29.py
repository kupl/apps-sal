n,k=map(int,input().split())
fact=[1]
for i in range(1,2*n):
  fact.append((fact[i-1]*(i+1))%(10**9+7))
factinv=[]
for i in range(n):
  factinv.append(pow(fact[i],10**9+5,10**9+7))
if k==1:
  print((n*(n-1))%(10**9+7))
elif k>=n-1:
  print((fact[2*n-2]*factinv[n-1]*factinv[n-2])%(10**9+7))
else:
  ans=1
  for i in range (k):
    ans=(ans+fact[n-1]*factinv[i]*factinv[n-i-2]*fact[n-2]*factinv[i]*factinv[n-i-3])%(10**9+7)
  print(ans)
