n,m,k=list(map(int,input().split()))
a=[]
ans=0
for i in range(n):
    a.append(input())
if k==1:
    for i in range(n):
        for j in range(m):
            if a[i][j]=='.':
                ans+=1
    print(ans)
    return
for i in range(n):
    l=0
    for j in range(m):
        if a[i][j]=='.':
            l+=1
        else:
            ans+=max(0,l-k+1)
            l=0
    ans+=max(0,l-k+1)
for i in range(m):
    l=0
    for j in range(n):
        if a[j][i]=='.':
            l+=1
        else:
            ans+=max(0,l-k+1)
            l=0
    ans+=max(0,l-k+1)
print(ans)

