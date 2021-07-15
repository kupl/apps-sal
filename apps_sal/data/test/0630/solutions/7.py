n,k=map(int,input().split())
s=list(map(int,input().split()))
ans=[[0] for i in range(n)]
for i in range(len(s)):
    s[i]-=1
for i in range(n):
    l=max(0,i-k)
    r=min(n-1,i+k)
    if s[i]==-1:   
        ans[i]=[r-l+1,r]
    else:    
        ans[i]=[ans[s[i]][0]+(r-l+1)-max(0,ans[s[i]][1]-l+1),r]
for j in range(n):
    print(ans[j][0],end=' ')

        

