def main():
  e=enumerate
  (n,t),*g=[list(map(int,t.split()))for t in open(0)]
  d=[0]
  g.sort()
  dp=[]
  d=[0]*t
  for a,b in g:
    p=d[:]
    for i in range(a,t):
      v=d[i-a]+b
      if v>p[i]:p[i]=v
    dp+=p,
    d=p
  a=m=0
  for(*_,v),(_,w)in zip(dp[-2::-1],g[::-1]):
    if w>m:m=w
    if v+m>a:a=v+m
  print(a)
main()
