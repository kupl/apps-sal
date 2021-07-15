n,m,k=map(int,input().split())
a=[int(x) for x in input().split()]+[10**9+5]
b=[int(x) for x in input().split()]+[10**9+5]

cnt=i=0
for ai in a:
  if cnt+ai>k: break;
  cnt+=ai; i+=1; 

j=0
for bi in b:
  if cnt+bi>k: break;
  cnt+=bi; j+=1;
  
ans=s=i+j
for i in reversed(range(i)):
  s-=1; cnt-=a[i];
  while cnt+b[j]<=k:
    s+=1; cnt+=b[j]; j+=1;
  ans=max(ans,s)
  
print(ans)
