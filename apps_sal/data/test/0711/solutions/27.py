MOD=10**9+7
UPPERLIMIT=2*10**5
MODMUL=[1, 1]+[0]*(UPPERLIMIT-1)
for i in range(2, UPPERLIMIT+1):
  MODMUL[i]=MODMUL[i-1]*i%MOD
MODDIV=[1]*UPPERLIMIT+[pow(MODMUL[-1], MOD-2, MOD)]
for i in range(UPPERLIMIT, 0, -1):
  MODDIV[i-1]=MODDIV[i]*i%MOD
def MODCOMB(n, r):
  return (((MODMUL[n]*MODDIV[r])%MOD)*MODDIV[n-r])%MOD

N, M=map(int, input().split())

from collections import defaultdict
def PrimeFactorization(x):
  out=defaultdict(int)
  for i in range(2, int(pow(x, 1/2))+1):
    while x%i==0:
      out[i]+=1
      x//=i
  if x>1:
    out[x]+=1
  return out

primenums=PrimeFactorization(M)
ans=1
for x in primenums.values():
  ans*=MODCOMB(N+x-1, N-1)
  ans%=MOD
  
print(ans)
