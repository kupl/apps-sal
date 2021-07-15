from itertools import product
s=input()
n=len(s)
ans=0
for p in product([0,1], repeat=n-1):
  wk=s[0]
  index=0
  for i in p:
    index+=1
    if i==0:
      wk+=s[index]
    else:
      ans+=int(wk)
      wk=s[index]
  if wk!="":
    ans+=int(wk)
print(ans)
