n,p=map(int,input().split())
s=input()
b=1
d=0
l=[0]*p
l[0]=1
ans=0
for i,c in enumerate(s[::-1]):
  if p==2 or p==5:
    if int(c)%p==0:
      ans+=n-i
  else:
    d+=int(c)*b
    d%=p
    l[d]+=1
    b*=10
    b%=p
if p!=2 and p!=5:
  for i in l:
    ans+=i*(i-1)//2
print(ans)
