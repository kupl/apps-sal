N,M=map(int,input().split())
MOD=10**9+7
 
def cmb(n, r, p):
  numerator = 1
  for i in range(n-r+1, n+1):
    numerator = numerator * i % p
  denominator = 1
  for j in range(1, r+1):
    denominator = denominator * j % p
  denominator = pow(denominator, p-2, p)
  return (numerator * denominator)%p
 
def factorization(n):
  l = []
  t = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if t%i==0:
      cnt=0
      while t%i==0:
        cnt+=1
        t //= i
      l.append([i, cnt])
  if t!=1:
    l.append([t, 1])
  if l==[]:
    l.append([n, 1])
  return l
 
ans=1
F=factorization(M)
for i in range(len(F)):
  f=F[i][1]
  ans*=cmb(f+N-1,f,MOD)
  ans%=MOD

if M==1:
  print(1)
else:
  print(ans)
