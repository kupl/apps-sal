MOD=10**9+7
N,M,K=map(int,input().split())

def powmod(a,p):
  if p==0:
    return 1
  elif p==1:
    return a
  else:
    pow2=powmod(a,p//2)
    if p%2==0:
      return (pow2**2)%MOD
    else:
      return (a*pow2**2)%MOD

def invmod(a):
  return powmod(a,MOD-2)

def comb_mod(n,r):
  nPr=1
  fact_r=1
  for i in range(r):
    nPr*=n-i
    nPr%=MOD
    fact_r*=r-i
    fact_r%=MOD  
  return (nPr*invmod(fact_r))%MOD

answer_tate=0
for d in range(1,N):
  answer_tate+=d*M**2*(N-d)
  answer_tate%=MOD
  
answer_yoko=0
for d in range(1,M):
  answer_yoko+=d*N**2*(M-d)
  answer_yoko%=MOD

comb=comb_mod(N*M-2,K-2)
print(comb*(answer_tate+answer_yoko)%MOD)
