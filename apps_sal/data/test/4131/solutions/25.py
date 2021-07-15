import bisect

n,m=list(map(int,input().split()))

ans=[]

re=[[] for _ in range(n)]



for _ in range(m):
  a=list(map(int,input().split()))
  re[a[0]-1].append(a[1])
  ans.append(a)
  
d=[]
for f in re:
  sor=[]
  
  new=sorted(list(set(f)))
  
  for i in f:
    c=bisect.bisect_left(new,i)
    sor.append(c+1)
    
  d.append(sor)
    
  
for x in ans:
  p=x[0]
  q=d[p-1].pop(0)
  print((str('{:0=6}'.format(p))+str('{:0=6}'.format(q))))
  


