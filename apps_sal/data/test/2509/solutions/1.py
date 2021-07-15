n,k=map(int,input().split())
ans=0
if k==0:print(n**2);return
for b in range(k+1,n+1):
    div=n//b  
    ans+=(b-k)*div
    rem=n%b
    ans+=max(0,rem-k+1)
print(ans)
