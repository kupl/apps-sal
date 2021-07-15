_,a,*l=map(int,open(0).read().split())
d={0:1}
for i in l:
  for k,v in d.copy().items(): d[i-a+k]=d.get(i-a+k,0)+v
print(d[0]-1)
