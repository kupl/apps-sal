n,k,q,*a=map(int,open(0).read().split())
ans=10**18
for y in set(a):
  c=[]
  tmp=[]
  for aa in a:
    if aa>=y:
      tmp.append(aa)
    else:
      if len(tmp)>=k:
        c+=sorted(tmp)[:len(tmp)-k+1]
      tmp=[]
  if len(tmp)>=k:
    c+=sorted(tmp)[:len(tmp)-k+1]
  if len(c)>=q:
    c.sort()
    x=c[q-1]
    ans=min(ans,x-y)
print(ans)
