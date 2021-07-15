import itertools
n,m,k=map(int,input().split())
a=list(itertools.accumulate(list(map(int,input().split()))))
b=list(itertools.accumulate(list(map(int,input().split()))))
a.insert(0,0)
a=[a[-i-1] for i in range(n+1)]
b.insert(0,0)
j=0
ans=0
for i in range(n+1):
  if a[i]<=k and j!=m+1:
    while a[i]+b[j]<=k:
      j+=1
      if j==m+1:
        break
    ans=max(ans,n-i+j-1)
print(ans)
