(n,),*t=[[*map(int,t.split())]for t in open(0)]
e=[f:=0]*n*4
for _ in t:
 for a,b in t:
  if a>0<b:
   for j,(c,d)in enumerate(t):
    f|=a<c<b>b-a!=d-c<d>0
    if b>c>a>0>d:t[j]=c,c+b-a
    if a<d<b>0>c:t[j]=d-b+a,d
for a,b in t:e[a]+=1;e[b]+=1
print('YNeos'[f+max(e[:-1])>1::2])
