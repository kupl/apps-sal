import sys
n=int(input())
caa=input()
cab=input()
cba=input()
cbb=input()
MOD=10**9+7
if n==2:
  print((1))
  return
dpa=[0]*n
dpb=[0]*n
dpa[0]=1
for i in range(1,n-1):
  dpa[i]=(dpa[i-1]+dpb[i-1])%MOD
  dpb[i]=dpa[i-1]
ans=dpa[n-2]
if cab=='A':
  if caa=='A':
    print((1))
  else:
    if cba=='B':
      print((pow(2,n-3,MOD)))
    else:
      print(ans)
else:
  if cbb=='B':
    print((1))
  else:
    if cba=='A':
      print((pow(2,n-3,MOD)))
    else:
      print(ans)

