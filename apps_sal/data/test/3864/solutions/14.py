mod=998244353
n=int(input())
a=[0,6,40]
if n==1:
  print(pow(2,-1,mod))
  return
if n==3:
  print(499122178)
  print(499122178)
  print(499122178)
  return
for i in range((n//2)+1):
  a.append((a[-1]*8-a[-2]*16)%mod)
if n%2==0:
  s=pow(2,n,mod)
  p=pow(s,-1,mod)
  c=n//2
  k=(c)%mod
  print(k)
  L=[k]
  k=(s*k)%mod
  q=n//2
  for i in range((n//2)-1):
    k+=a[i]
    po=(k*p)%mod
    L.append(po)
    print(po)
  for i in range(q):
    print(L[q-i-1])
else:
  s=pow(2,n,mod)
  p=pow(s,-1,mod)
  
  k=(n*pow(2,-1,mod))%mod
  print(k)
  L=[k]
  k=(s*k)%mod
  q=n//2
  for i in range((n//2)-1):
    k+=a[i]
    po=(k*p)%mod
    L.append(po)
    print(po)
  k+=a[i+1]
  po=(k*p)%mod
  print(po)
  for i in range(q):
    print(L[q-i-1])
