N=int(input())
s=[0]*N
s_nz=[101]*N
res=0
for i in range(N) :
  s[i]=int(input())
  if s[i]%10!=0 :
    s_nz[i]=s[i]
  res+=s[i]
if res%10==0 :
  if min(s_nz)==101 :
    res=0
  else :
    res-=min(s_nz)
print(res)


