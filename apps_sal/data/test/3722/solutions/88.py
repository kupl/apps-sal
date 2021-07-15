mod=10**9+7

n=int(input())
if n==2 or n==3:
  print(1)
  return
c=[input() for _ in range(4)]
if c[0]==c[1]=='A' or c[1]==c[3]=='B':
  print(1)
elif (c[0]=='B' and c[1]==c[2]=='A') or (c[3]=='A' and c[1]==c[2]=='B'):
  fact=[1]
  for i in range(1,n+1):
    fact.append((fact[-1]*i)%mod)
  rfact=[pow(fact[-1],mod-2,mod)]
  for i in range(n,0,-1):
    rfact.append((rfact[-1]*i)%mod)
  rfact=rfact[::-1]
  ans=0
  for i in range(n-1):
    if 2*i-(n-2)<0:
      continue
    ans+=fact[i]*rfact[n-2-i]*rfact[2*i-(n-2)]
  print(ans%mod)
else:
  print(pow(2,n-3,mod))
