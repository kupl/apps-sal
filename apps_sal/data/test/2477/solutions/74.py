n,k,*A=map(int,open(0).read().split());l=1;r=max(A)
while l!=r:
  c=(l+r)//2
  if k>=sum(-(-a//c)-1 for a in A):r=c
  else:l=c+1
print(l)
