from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m=nii()
ab=[lnii() for i in range(n)]
cd=[lnii() for i in range(m)]

ans=[]
for a,b in ab:
  min_dist=10**10
  for i in range(m):
    c,d=cd[i]
    if abs(a-c)+abs(b-d)<min_dist:
      t_ans=i
      min_dist=abs(a-c)+abs(b-d)
  ans.append(t_ans+1)

for i in ans:
  print(i)
