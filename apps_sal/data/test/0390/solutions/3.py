n,a,b=map(int,input().strip().split())
l=list(map(int,input().strip().split()))
c=min(a,b)
ans=0
for i in range(n//2):
    if l[i]!=2 and l[n-1-i]!=2 and l[i]!=l[n-1-i]:
        print (-1)
        return
    if l[i]==2 and l[n-1-i]==0:
        ans=ans+a
        continue
    if l[i]==2 and l[n-1-i]==1:
        ans=ans+b
        continue
    if l[i]==0 and l[n-1-i]==2:
        ans=ans+a
        continue
    if l[i]==1 and l[n-1-i]==2:
        ans=ans+b
        continue
    if l[i]==2 and l[n-1-i]==2:
        ans=ans+2*c
        continue
if (n%2==1 and l[n//2]==2):
    ans=ans+c
print (ans)
