n=int(input())
s=list(map(ord,list(input())))
for i in range(n):s[i]-=97

from random import randint
roli_mod=1370757747362922367
roli_r=randint(2,roli_mod-2)
roli=[0]
roli_rr=1
for i in range(n):
  roli.append((roli[-1]+roli_rr*s[i])%roli_mod)
  roli_rr*=roli_r
  roli_rr%=roli_mod
def roli_hash(i,j):return ((roli[j+1]-roli[i]+roli_mod)%roli_mod)*pow(roli_r,roli_mod-1-i,roli_mod)%roli_mod
def roli_check(i1,j1,i2,j2):return roli_hash(i1,j1)==roli_hash(i2,j2)

ok=0
ng=(n+1)//2+1
while ok+1!=ng:
  i=(ok+ng)//2
  d={}
  f=False
  for j in range(n-i+1):
    h=roli_hash(j,j+i-1)
    if h in d:
      if j-d[h]>=i:
        f=True
        break
    else:d[h]=j
  if f:ok=i
  else:ng=i
print(ok)
