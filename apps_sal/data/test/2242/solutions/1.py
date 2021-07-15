ans=0
S=input()
a=len(S)
k=0
c=dict()
mod=2019
s=1
c[0]=1
for i in range(a):
  k+=(s*int(S[a-i-1]))
  k%=mod
  s*=10
  s%=mod
  if k in c:
    c[k]+=1
  else:
    c[k]=1
for i in c:
  ans+=c[i]*(c[i]-1)//2
print(ans)
