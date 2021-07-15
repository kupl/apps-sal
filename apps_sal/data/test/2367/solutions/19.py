MOD=10**9+7
UPPERLIMIT=2*(10**5)+1
MODMUL=[1, 1]+[0]*(UPPERLIMIT-1)
for i in range(2, UPPERLIMIT+1):
  MODMUL[i]=MODMUL[i-1]*i%MOD
MODDIV=[1]*UPPERLIMIT+[pow(MODMUL[-1], MOD-2, MOD)]
for i in range(UPPERLIMIT, 0, -1):
  MODDIV[i-1]=MODDIV[i]*i%MOD

H, W, A, B=map(int, input().split())

ans=(((MODMUL[H+W-2]*MODDIV[H-1])%MOD)*MODDIV[W-1])%MOD

x=[MODMUL[H-A+B+i-1]*MODDIV[B-1]*MODDIV[H-A+i]%MOD for i in range(A)]
y=[MODMUL[W+A-B-i-1]*MODDIV[W-B]*MODDIV[A-i-1]%MOD for i in range(A)]
for i in range(A-1, 0, -1):
  x[i]-=x[i-1]

for i in range(A):
  ans-=(x[i]*y[i]%MOD)
  ans%=MOD
  
print(ans)
