A,B,X=map(int,input().split())
ans=0
if A*1000000000+B*10<=X:
    ans=1000000000
for d in range(1,10):
    x=(X-B*d)//A
    if 10**(d-1)<=x and x<10**d:
        ans=max(ans,x)
    elif x>=10**d:
        ans=max(ans,10**d-1)
print(ans)
