n,p=list(map(int,input().split()))
s=input()
ans=0
p-=1
if(n%2==1 and p==n//2 and n!=1):
    p-=1
    ans+=1
cnt=0
for i in range(n):
    if(n-1-i<=i):
        break
    if(s[i]!=s[n-1-i]):
        cnt+=1

if(p>=n//2 and n!=1):
    h=""
    for i in range(n-1,-1,-1):
        h+=s[i]
    s=h
    p=n-1-p
r=0
l=0
rr=0
ll=0
for i in range(p):
    if(s[i]!=s[n-1-i]):
        ans+=min(26-abs(ord(s[i])-ord(s[n-1-i])),abs(ord(s[i])-ord(s[n-1-i])))
        r+=1
        rr=max(rr,p-i)
for i in range(p+1,n//2):
    if(s[i]!=s[n-1-i]):
        ans+=min(26-abs(ord(s[i])-ord(s[n-1-i])),abs(ord(s[i])-ord(s[n-1-i])))
        l+=1
        ll=max(ll,i-p)
ans+=min(26-abs(ord(s[p])-ord(s[n-1-p])),abs(ord(s[p])-ord(s[n-1-p])))
ans+=ll+rr+min(ll,rr)
print(ans)

