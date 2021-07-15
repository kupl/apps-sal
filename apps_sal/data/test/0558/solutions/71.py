N,M,K=map(int,input().split())
MOD=998244353

#逆元を定義する
def inv(a):
  return pow(a,MOD-2,MOD)

#「n!」の剰余を求める
fact=[0,1]
for i in range(2,N+1):
  fact.append((fact[-1]*i)%MOD)

#nCr(MOD)を求める
def choose(n,r):
  if r==0 or r==n:
    return 1
  else:
    return fact[n]*inv(fact[r])*inv(fact[n-r])%MOD

#(M-1)**n(MOD)を求める
exp=[1]
for i in range(1,N):
  exp.append((exp[-1]*(M-1))%MOD)  
  

#答えを計算する
ans=0
for i in range(K+1):
  ans+=(M*choose(N-1,i)*exp[N-1-i]%MOD)  
  ans%=MOD
print(ans)  
