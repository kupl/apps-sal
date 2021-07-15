n,m,k=map(int,input().split());A,B=eval("[0]+[*map(int,input().split())],"*2);s=t=x=0;j=m
for i in range(n+1):s+=A[i];A[i]=s
for i in range(m+1):t+=B[i];B[i]=t
for i in range(n+1):
  if A[i]>k:break
  while B[j]>k-A[i]:j-=1
  x=max(x,i+j)
print(x)
