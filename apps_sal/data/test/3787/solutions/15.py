n,a,b=map(int,input().split())
ans=[];L=[a]*b;x=a*b-n;ct=1
if a+b>n+1 or x<0:print(-1);return
for i in range(b-1,0,-1):
 y=min(a-1,x);L[i]-=y;x-=y
for i in L:
 l=[]
 for j in range(i):
  l+=[str(ct)];ct+=1
 ans+=[' '.join(l)]
print(*reversed(ans))
