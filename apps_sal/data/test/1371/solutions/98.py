MOD=10**9+7
UPPERLIMIT=10**4
MODMUL=[1, 1]+[0]*(UPPERLIMIT-1)
for i in range(2, UPPERLIMIT+1):
  MODMUL[i]=MODMUL[i-1]*i%MOD
MODDIV=[1]*UPPERLIMIT+[pow(MODMUL[-1], MOD-2, MOD)]
for i in range(UPPERLIMIT, 0, -1):
  MODDIV[i-1]=MODDIV[i]*i%MOD
def MODCOMB(n, r):
  return (((MODMUL[n]*MODDIV[r])%MOD)*MODDIV[n-r])%MOD

S=int(input())
if S<3:
  print(0)
  return
  
ans=0
T=S//3
for i in range(1, T+1):
  x=S-i*3
  ans=(ans+MODCOMB(x+i-1, x))%MOD
  
print(ans)
