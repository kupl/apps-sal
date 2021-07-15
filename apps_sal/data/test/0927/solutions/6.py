n,m=map(int,input().split())
A=reversed(sorted(map(int,input().split())))
M=[2,5,5,4,5,6,3,7,6]
D={}
E={}
for a in A:
    if M[a-1] in D:
        continue
    else:
        D[M[a-1]]=a
        E[a]=M[a-1]
S=list(reversed(sorted(E)))
        
dp=[0]*(n+2)
for i in range(1,n+2):
    cnt=-1
    for d in D:
        if i-d>=0:
            if dp[i-d]!=-1:
                cnt=max(dp[i-d]+1,cnt)
    dp[i]=cnt    
k=dp[n]
ans=""

while k>0:
    for s in S:
        x=E[s]
        if n-x<0:
            continue
        if dp[n-x]==k-1:
            ans+=str(s)
            k-=1
            n-=x
            break
print(ans)
