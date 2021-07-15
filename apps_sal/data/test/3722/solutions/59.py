mod=10**9+7

n=int(input())
if n==2 or n==3:
  print(1)
  return
caa=input()
cab=input()
cba=input()
cbb=input()

fact=[1]
for i in range(1,3001):
  fact.append((fact[-1]*i)%mod)
revfact=[pow(fact[-1],mod-2,mod)]
for i in range(3000,0,-1):
  revfact.append((revfact[-1]*i)%mod)
revfact=revfact[::-1]

def comb(n,r):
  return (fact[n]*revfact[r]*revfact[n-r])%mod

if cab=='A' and cba=='A':
  if caa=='A':
    print(1)
  else:
    ans=0
    for cnta in range(1,n):
      sukima=cnta-1
      cntb=n-1-cnta
      if cntb>sukima:
        continue
      else:
        ans+=comb(sukima,cntb)
    print(ans%mod)
elif cab=='A' and cba=='B':
  if caa=='A':
    print(1)
  else:
    print(pow(2,n-3,mod))
elif cab=='B' and cba=='A':
  if cbb=='B':
    print(1)
  else:
    print(pow(2,n-3,mod))
elif cab=='B' and cba=='B':
  if cbb=='B':
    print(1)
  else:
    ans=0
    for cntb in range(1,n):
      sukima=cntb-1
      cnta=n-1-cntb
      if cnta>sukima:
        continue
      else:
        ans+=comb(sukima,cnta)
    print(ans%mod)
