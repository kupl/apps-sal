import itertools
n,m,q=map(int,input().split())
d=[list(map(int,input().split())) for i in range(q)]
ans=0
for i in list(itertools.combinations_with_replacement(list(range(1,m+1)), n)):
  a=list(i)
  hantei=0
  for j in range(q):
    if (a[d[j][1]-1]-a[d[j][0]-1])==d[j][2]:
      hantei+=d[j][3]
  ans=max(ans,hantei)
print(ans)
